# Product Catalog Service

A FastAPI-based microservice for managing product information.

## Features

- Create, read, update, and delete product information
- Search products by category
- RESTful API endpoints
- OpenAPI documentation
- Health check endpoint

## Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

## Installation

1. Clone the repository
2. Navigate to the service directory:
   ```bash
   cd product-service
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Service

To run the service locally:

```bash
uvicorn main:app --reload --port 8001
```

The service will be available at `http://localhost:8001`

## API Documentation

Once the service is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:8001/docs`
- ReDoc: `http://localhost:8001/redoc`

## API Endpoints

- `GET /`: Health check endpoint
- `POST /products/`: Create a new product
- `GET /products/`: Get all products
- `GET /products/{product_id}`: Get product by ID
- `PUT /products/{product_id}`: Update product
- `DELETE /products/{product_id}`: Delete product
- `GET /products/category/{category}`: Get products by category

## Example Requests

### Create Product
```bash
curl -X POST "http://localhost:8001/products/" \
     -H "Content-Type: application/json" \
     -d '{"name": "Laptop", "description": "High-performance laptop", "price": 999.99, "category": "Electronics"}'
```

### Get Products by Category
```bash
curl "http://localhost:8001/products/category/Electronics"
```

## Deployment

This service is configured for deployment on Choreo. The `choreo.yaml` file contains the necessary configuration for deployment.

## License

MIT 