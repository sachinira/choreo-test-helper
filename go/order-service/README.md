# Order Service

A Fiber-based microservice for managing orders.

## Features

- Create, read, update, and delete orders
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
   cd order-service
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

The service will be available at `http://localhost:3000`

## API Documentation

The OpenAPI specification is available in the `openapi.yaml` file. You can use tools like Swagger UI or ReDoc to view the interactive documentation.

## API Endpoints

- `GET /`: Health check endpoint
- `POST /orders`: Create a new order
- `GET /orders`: Get all orders
- `GET /orders/{id}`: Get order by ID
- `PUT /orders/{id}`: Update order
- `DELETE /orders/{id}`: Delete order

## Example Requests

### Create Order
```bash
curl -X POST "http://localhost:3000/orders" \
     -H "Content-Type: application/json" \
     -d '{"user_id": "user123", "product_id": "prod456", "quantity": 2, "total_amount": 199.98, "status": "pending"}'
```

### Get Order
```bash
curl "http://localhost:3000/orders/order123"
```

## Deployment

This service is configured for deployment on Choreo. The `choreo.yaml` file contains the necessary configuration for deployment.

## License

MIT 