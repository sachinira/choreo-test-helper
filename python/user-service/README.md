# User Management Service

A FastAPI-based microservice for managing user data with CRUD operations.

## Features

- Create new users
- Retrieve user information
- Update existing users
- Delete users
- List all users

## API Endpoints

- `GET /` - Health check endpoint
- `POST /users/` - Create a new user
- `GET /users/` - Get all users
- `GET /users/{user_id}` - Get a specific user by ID
- `PUT /users/{user_id}` - Update a user
- `DELETE /users/{user_id}` - Delete a user

## User Model

```json
{
    "id": "integer (optional)",
    "username": "string",
    "email": "string",
    "full_name": "string"
}
```

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Service

To start the service locally:

```bash
python main.py
```

The service will start on `http://localhost:8000`

## API Documentation

Once the service is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Development

This service uses:
- FastAPI for the web framework
- Pydantic for data validation
- Uvicorn as the ASGI server

## Note

This service currently uses an in-memory database for demonstration purposes. In a production environment, you would want to replace this with a persistent database solution. 