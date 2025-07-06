# app/schemas.py

from pydantic import BaseModel,EmailStr

class ItemCreate(BaseModel):
    name: str
    description: str

class ItemOut(ItemCreate):
    id: int

    class Config:
        orm_mode = True
class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class OrderCreate(BaseModel):
    order_id: str
    quantity: int
