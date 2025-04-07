# Choreo Test Helper

A collection of microservices and OpenAPI specifications designed for testing and demonstration purposes in Choreo, a cloud-native application development platform.

## Project Structure

```
.
├── go/                    # Go-based microservices
│   ├── notification-service/  # Service for managing notifications
│   ├── order-service/        # Service for managing orders
│   └── payment-service/      # Service for managing payments
├── python/                # Python-based microservices
│   ├── product-service/      # Service for managing product catalog
│   └── user-service/         # Service for managing user data
└── openapis/             # OpenAPI specifications
```

## Services Overview

### Go Services

1. **Order Service** (Port: 3000)
   - Manages order creation, retrieval, and processing
   - RESTful API with OpenAPI documentation
   - Built with Go Fiber framework

2. **Payment Service** (Port: 3001)
   - Handles payment processing and transaction management
   - Integrates with order service
   - Built with Go Fiber framework

3. **Notification Service** (Port: 3002)
   - Manages notification delivery and tracking
   - Supports multiple notification types
   - Built with Go Fiber framework

### Python Services

1. **User Service** (Port: 8000)
   - Manages user accounts and authentication
   - Built with FastAPI framework

2. **Product Service** (Port: 8001)
   - Manages product catalog and inventory
   - Built with FastAPI framework

## Prerequisites

- Go 1.21 or higher (for Go services)
- Python 3.11 or higher (for Python services)
- Docker (optional, for containerized deployment)

## Getting Started

Each service has its own README with specific setup instructions. Navigate to the respective service directory for detailed information:

- [Order Service](go/order-service/README.md)
- [Payment Service](go/payment-service/README.md)
- [Notification Service](go/notification-service/README.md)
- [Product Service](python/product-service/README.md)
- [User Service](python/user-service/README.md)

## Deployment

All services are configured for deployment on Choreo using `choreo.yaml` configuration files. Each service includes:

- Health check endpoints
- Port configurations
- Environment variables
- Build commands

## API Documentation

Each service provides OpenAPI documentation accessible through:
- Go services: OpenAPI specification in `openapi.yaml`
- Python services: Swagger UI at `/docs` and ReDoc at `/redoc`

## License

MIT
