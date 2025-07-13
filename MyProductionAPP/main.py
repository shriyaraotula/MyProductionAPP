# app/main.py

import threading
import os
from datetime import timedelta
from typing import List
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.openapi.utils import get_openapi
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from .schemas import OrderCreate
from .wait_for_db import wait_for_postgres
from . import crud, models, schemas
from .auth import (
    ALGORITHM, SECRET_KEY, create_access_token,
    get_password_hash, verify_password
)
from .database import Base, SessionLocal, engine

load_dotenv()

# === Optional Kafka ===
ENABLE_KAFKA = os.getenv("ENABLE_KAFKA", "1") == "1"
if ENABLE_KAFKA:
    from .kafka.consumer import start_consumer
    from .kafka.producer import send_order_to_kafka
else:
    def send_order_to_kafka(_): pass

# === DB Setup ===
wait_for_postgres(
    host=os.getenv("DB_HOST", "localhost"),
    db=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    port=int(os.getenv("DB_PORT", 5432)),
)
Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/health")
def health_check():
    return {"status": "ok"}


# === DB Dependency ===
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# === OpenAPI Auth Header ===
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="MyProductionAPP",
        version="1.0.0",
        description="My app with JWT authentication",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.get("/protected")
def read_protected(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@app.post("/items/", response_model=schemas.ItemOut)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)


@app.get("/items/", response_model=List[schemas.ItemOut])
def read_items(db: Session = Depends(get_db)):
    return crud.get_items(db)


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None:
        raise credentials_exception
    return user


@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    new_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg": "User registered"}


@app.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/order")
def place_order(order: OrderCreate):
    send_order_to_kafka(order.dict())
    return {"status": "queued", "order_id": order.order_id}


@app.on_event("startup")
def start_kafka_consumer():
    if ENABLE_KAFKA:
        thread = threading.Thread(target=start_consumer, daemon=True)
        thread.start()
