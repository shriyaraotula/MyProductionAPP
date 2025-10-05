# Quick Start Guide

This guide will help you get MyProductionAPP up and running in minutes.

## 🚀 Quick Start with Docker (Recommended)

The fastest way to get started is using Docker Compose:

```bash
# 1. Clone the repository
git clone https://github.com/shriyaraotula/MyProductionAPP.git
cd MyProductionAPP

# 2. Create environment file
cp .env.example .env

# 3. Start the application
docker-compose up -d

# 4. Check if it's running
curl http://localhost:8000/docs
```

That's it! The API is now running at `http://localhost:8000`

## 📖 API Documentation

Visit `http://localhost:8000/docs` for interactive API documentation (Swagger UI)

## 🔐 Test the API

### 1. Register a new user

```bash
curl -X POST "http://localhost:8000/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "testpassword"
  }'
```

### 2. Login to get access token

```bash
curl -X POST "http://localhost:8000/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=testpassword"
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### 3. Create an item (authenticated)

```bash
curl -X POST "http://localhost:8000/items/" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Item",
    "description": "This is a test item"
  }'
```

### 4. Get all items (authenticated)

```bash
curl -X GET "http://localhost:8000/items/" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## 🛠️ Development Setup (Without Docker)

If you prefer to run locally without Docker:

```bash
# 1. Install Python 3.9+
python --version

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up PostgreSQL database
# Install PostgreSQL and create a database

# 5. Configure .env file
cp .env.example .env
# Edit .env with your database credentials

# 6. Run the application
uvicorn main:app --reload
```

## 📊 Checking Logs

```bash
# View logs
docker-compose logs -f app

# View database logs
docker-compose logs -f db
```

## 🛑 Stopping the Application

```bash
docker-compose down

# To also remove volumes
docker-compose down -v
```

## ❓ Troubleshooting

### Port already in use
If port 8000 or 5432 is already in use, modify the ports in `docker-compose.yml`:

```yaml
ports:
  - "8001:8000"  # Change host port
```

### Database connection issues
Wait a few seconds after starting for the database to be ready. The app will automatically retry the connection.

### Permission denied errors
On Linux, you might need to run with sudo:
```bash
sudo docker-compose up -d
```

## 📚 Next Steps

- Read the full [README.md](README.md) for detailed information
- Check [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
- Explore the API at `http://localhost:8000/docs`

## 🆘 Need Help?

Open an issue on GitHub if you encounter any problems!
