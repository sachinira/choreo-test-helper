# User Management Service

A FastAPI-based microservice for managing user data with CRUD operations and AI-powered question answering.

## Features

- Create new users
- Retrieve user information
- Update existing users
- Delete users
- List all users
- AI-powered question answering through OpenAI integration

## API Endpoints

- `GET /` - Health check endpoint
- `POST /users/` - Create a new user
- `GET /users/` - Get all users
- `GET /users/{user_id}` - Get a specific user by ID
- `PUT /users/{user_id}` - Update a user
- `DELETE /users/{user_id}` - Delete a user
- `POST /ask` - Ask questions to the AI assistant

## User Model

```json
{
    "id": "integer (optional)",
    "username": "string",
    "email": "string",
    "full_name": "string"
}
```

## Question Model

```json
{
    "question": "string"
}
```

## Prerequisites

- Python 3.7+
- pip (Python package manager)
- OpenAI API access (for AI question answering feature)

## Environment Variables

The service requires the following environment variables:
- `CHOREO_OPENAICONNECTIONPROJECT_OPENAI_API_KEY`: Your OpenAI API key
- `CHOREO_OPENAICONNECTIONPROJECT_SERVICEURL`: OpenAI service URL

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your environment variables in a `.env` file

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
- OpenAI for AI-powered question answering

## Note

This service currently uses an in-memory database for demonstration purposes. In a production environment, you would want to replace this with a persistent database solution. 