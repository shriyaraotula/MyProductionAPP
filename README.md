# MyProductionAPP

A production-ready FastAPI application with JWT authentication and PostgreSQL database integration.

## What is MyProductionAPP?

MyProductionAPP is a **backend application** built with FastAPI that provides:
- RESTful API endpoints for managing items
- User registration and authentication with JWT tokens
- PostgreSQL database integration
- Secure password hashing with bcrypt
- OAuth2 password bearer authentication

## How is this different from GitHub Copilot Workspace?

**MyProductionAPP** and **GitHub Copilot Workspace** serve completely different purposes:

### MyProductionAPP (This Repository)
- **Type**: Production application/software
- **Purpose**: A backend API service that runs on servers to handle user authentication, data management, and business logic
- **What it does**: Provides HTTP endpoints that clients can call to register users, login, manage items, etc.
- **Runtime**: Runs as a web service (FastAPI server) with PostgreSQL database
- **Users**: End users of your application who interact with the API

### GitHub Copilot Workspace
- **Type**: Development tool/IDE feature
- **Purpose**: An AI-powered development environment that helps developers write code
- **What it does**: Provides intelligent code suggestions, completions, and assistance while you're developing applications like MyProductionAPP
- **Runtime**: Runs in your development environment (VS Code, GitHub.com, etc.)
- **Users**: Developers who are writing code

**In summary**: GitHub Copilot Workspace is a **tool you use to build** applications, while MyProductionAPP is the **application being built**. It's like comparing a hammer (tool) to a house (product).

## Features

- ✅ User registration and authentication
- ✅ JWT token-based authorization
- ✅ CRUD operations for items
- ✅ PostgreSQL database with SQLAlchemy ORM
- ✅ Password hashing with bcrypt
- ✅ OpenAPI/Swagger documentation
- ✅ Database connection retry logic

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT (JSON Web Tokens) with python-jose
- **Password Hashing**: bcrypt via passlib
- **Environment Management**: python-dotenv

## Project Structure

```
MyProductionAPP/
├── __init__.py          # Package initialization
├── main.py              # FastAPI application and endpoints
├── models.py            # SQLAlchemy database models
├── schemas.py           # Pydantic schemas for request/response validation
├── crud.py              # Database CRUD operations
├── database.py          # Database connection and session management
├── auth.py              # JWT token creation and verification
├── utils.py             # Password hashing utilities
└── wait_for_db.py       # Database connection retry logic
```

## API Endpoints

### Authentication
- `POST /register` - Register a new user
  - Body: `{"email": "user@example.com", "password": "password123"}`
- `POST /login` - Login and receive JWT token
  - Body: `{"username": "user@example.com", "password": "password123"}`

### Items Management
- `POST /items/` - Create a new item (requires authentication)
  - Body: `{"name": "Item Name", "description": "Item Description"}`
- `GET /items/` - Get all items (requires authentication)

### Protected Routes
- `GET /protected` - Test endpoint that requires authentication

## Setup and Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/shriyaraotula/MyProductionAPP.git
   cd MyProductionAPP
   ```

2. **Set up environment variables**
   Create a `.env` file with:
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/dbname
   DB_HOST=localhost
   DB_PORT=5432
   POSTGRES_DB=myapp
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=yourpassword
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi sqlalchemy psycopg2-binary python-jose[cryptography] passlib[bcrypt] python-dotenv
   ```

4. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API documentation**
   Open your browser to `http://localhost:8000/docs` for interactive Swagger UI

## Development

This application was developed with the assistance of AI tools but is a standalone production application that can be deployed and run independently.

## Security Notes

⚠️ **Important**: Before deploying to production:
- Change the `SECRET_KEY` in `auth.py` to a strong, random secret
- Use environment variables for all sensitive configuration
- Enable HTTPS/TLS for all API endpoints
- Implement rate limiting and other security best practices
- Regular security audits and dependency updates

## License

This project is available for educational and development purposes.
