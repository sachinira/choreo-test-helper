# Payment Service

A Fiber-based microservice for managing payments.

## Features

- Create and retrieve payment information
- Get payments by order ID
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
   cd payment-service
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

The service will be available at `http://localhost:3001`

## API Documentation

The OpenAPI specification is available in the `openapi.yaml` file. You can use tools like Swagger UI or ReDoc to view the interactive documentation.

## API Endpoints

- `GET /`: Health check endpoint
- `POST /payments`: Create a new payment
- `GET /payments`: Get all payments
- `GET /payments/{id}`: Get payment by ID
- `GET /payments/order/{order_id}`: Get payments by order ID

## Example Requests

### Create Payment
```bash
curl -X POST "http://localhost:3001/payments" \
     -H "Content-Type: application/json" \
     -d '{"order_id": "order123", "amount": 199.98, "status": "completed", "method": "credit_card", "timestamp": "2024-01-01T12:00:00Z"}'
```

### Get Payments by Order
```bash
curl "http://localhost:3001/payments/order/order123"
```

## Deployment

This service is configured for deployment on Choreo. The `choreo.yaml` file contains the necessary configuration for deployment.

## License

MIT 