# Notification Service

A Fiber-based microservice for managing notifications.

## Features

- Create and retrieve notifications
- Get notifications by user ID
- Mark notifications as read
- RESTful API endpoints
- OpenAPI documentation
- Health check endpoint

## Prerequisites

- Go 1.21 or higher
- Go modules enabled

## Installation

1. Clone the repository
2. Navigate to the service directory:
   ```bash
   cd notification-service
   ```
3. Install dependencies:
   ```bash
   go mod download
   ```

## Running the Service

To run the service locally:

```bash
go run main.go
```

The service will be available at `http://localhost:3002`

## API Documentation

The OpenAPI specification is available in the `openapi.yaml` file. You can use tools like Swagger UI or ReDoc to view the interactive documentation.

## API Endpoints

- `GET /`: Health check endpoint
- `POST /notifications`: Create a new notification
- `GET /notifications`: Get all notifications
- `GET /notifications/{id}`: Get notification by ID
- `GET /notifications/user/{user_id}`: Get notifications by user ID
- `PUT /notifications/{id}/read`: Mark notification as read

## Example Requests

### Create Notification
```bash
curl -X POST "http://localhost:3002/notifications" \
     -H "Content-Type: application/json" \
     -d '{"user_id": "user123", "type": "order_update", "message": "Your order has been shipped", "timestamp": "2024-01-01T12:00:00Z"}'
```

### Get User Notifications
```bash
curl "http://localhost:3002/notifications/user/user123"
```

### Mark Notification as Read
```bash
curl -X PUT "http://localhost:3002/notifications/notif123/read"
```

## Deployment

This service is configured for deployment on Choreo. The `choreo.yaml` file contains the necessary configuration for deployment.

## License

MIT 