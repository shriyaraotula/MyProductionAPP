# MyProductionAPP

A production-ready FastAPI application with PostgreSQL database, JWT authentication, and Docker support.

## Features

- **FastAPI** - Modern, fast web framework for building APIs
- **PostgreSQL** - Robust relational database
- **JWT Authentication** - Secure user authentication with JSON Web Tokens
- **Docker Support** - Easy deployment with Docker and Docker Compose
- **SQLAlchemy ORM** - Powerful database abstraction layer
- **User Registration & Login** - Complete user management system
- **Item Management** - CRUD operations for items

## Tech Stack

- Python 3.9+
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT (python-jose)
- Passlib (bcrypt)
- Docker & Docker Compose

## Project Structure

```
MyProductionAPP/
├── main.py           # FastAPI application entry point
├── models.py         # SQLAlchemy database models
├── schemas.py        # Pydantic schemas for request/response validation
├── crud.py           # Database CRUD operations
├── auth.py           # Authentication utilities (JWT, password hashing)
├── database.py       # Database configuration and session management
├── utils.py          # Utility functions
├── wait_for_db.py    # Database connection retry logic
└── __init__.py       # Package initialization
```

## Getting Started

### Prerequisites

- Python 3.9 or higher
- PostgreSQL database
- Docker and Docker Compose (optional, for containerized deployment)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/shriyaraotula/MyProductionAPP.git
cd MyProductionAPP
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file (see `.env.example` for reference):
```bash
cp .env.example .env
```

5. Configure your environment variables in `.env`:
```
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
DB_HOST=localhost
DB_PORT=5432
POSTGRES_DB=myapp
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
SECRET_KEY=your-secret-key-here
```

### Running the Application

#### Option 1: Local Development

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

#### Option 2: Docker Compose

```bash
docker-compose up -d
```

### API Documentation

Once the application is running, visit:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Authentication

- `POST /register` - Register a new user
  ```json
  {
    "email": "user@example.com",
    "password": "securepassword"
  }
  ```

- `POST /login` - Login and get access token
  ```json
  {
    "username": "user@example.com",
    "password": "securepassword"
  }
  ```

### Items

- `POST /items/` - Create a new item (requires authentication)
- `GET /items/` - Get all items (requires authentication)

### Protected Routes

- `GET /protected` - Test protected endpoint (requires authentication)

## Authentication

The API uses JWT (JSON Web Tokens) for authentication. After logging in, you'll receive an access token that must be included in the Authorization header for protected endpoints:

```
Authorization: Bearer <your_access_token>
```

## Development

### Running Tests

```bash
pytest
```

### Code Quality

```bash
# Format code
black .

# Lint code
flake8 .

# Type checking
pyright
```

## Security Notes

- Change the `SECRET_KEY` in production
- Use environment variables for sensitive data
- Enable HTTPS in production
- Implement rate limiting for production use
- Review and update CORS settings as needed

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please read CONTRIBUTING.md for guidelines.

## Support

For issues and questions, please open an issue on GitHub.
