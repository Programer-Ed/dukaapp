## Duka Moja API Documentation
### Table of Contents
1. Overview
2. Getting Started
3. Base URL
4. Authentication
- User Registration
- User Login
5. Product Management
- Get All Products
- Get a Single Product
- Create a Product
- Update a Product
- Delete a Product
6. Order Management
- Create an Order
- Get Orders by User
- Get All Orders
- Update Order Status
- Delete an Order
7. Error Handling
8. Rate Limiting
9.Contact Information

## Overview
The Duka Moja API serves as the backend interface for the Duka Moja eCommerce platform, enabling the management of users, products, orders, and other functionalities. This API is built using RESTful principles, ensuring it is intuitive and easy to use for developers.

## Getting Started
To interact with the Duka Moja API, you will need a basic understanding of HTTP methods, JSON format, and the ability to make requests using tools like Postman or cURL.

### Prerequisites
- An API client (Postman, Insomnia, cURL)
- Basic knowledge of RESTful API principles
- Familiarity with JSON format
1. Base URL
All API endpoints can be accessed through the following base URL:

http://localhost:5000/api

2. Authentication
- User Registration
- Endpoint: POST /users

*Registers a new user*.

Request Body:
json

{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "password": "yourpassword"
}
Response:
201 Created

json

{
  "message": "User registered successfully",
  "user": {
    "_id": "60e6c1d18b456f0e74f6d3b5",
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
}

*User Login*
- Endpoint: POST /auth/login

Authenticates a user and returns a JWT token for future requests.

Request Body:
json

{
  "email": "john.doe@example.com",
  "password": "yourpassword"
}
Response:
200 OK

json

{
  "token": "your_jwt_token_here",
  "user": {
    "_id": "60e6c1d18b456f0e74f6d3b5",
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
}

*Product Management*
- Get All Products
- Endpoint: GET /products

Retrieves a list of all products.

Response:
200 OK

json

[
  {
    "_id": "60e6c1d18b456f0e74f6d3b5",
    "name": "Wireless Headphones",
    "description": "High-quality wireless headphones with noise cancellation.",
    "price": 89.99,
    "category": "Electronics",
    "image": "https://example.com/image.jpg",
    "createdAt": "2024-10-18T12:34:56.789Z",
    "updatedAt": "2024-10-18T12:34:56.789Z"
  }
]

*Get a Single Product*
- Endpoint: GET /products/:id

- Retrieves detailed information about a single product by its ID.

Response:
200 OK

json

{
  "_id": "60e6c1d18b456f0e74f6d3b5",
  "name": "Wireless Headphones",
  "description": "High-quality wireless headphones with noise cancellation.",
  "price": 89.99,
  "category": "Electronics",
  "image": "https://example.com/image.jpg",
  "createdAt": "2024-10-18T12:34:56.789Z",
  "updatedAt": "2024-10-18T12:34:56.789Z"
}

*Create a Product*
- Endpoint: POST /products

- Creates a new product.

Request Body:
json

{
  "name": "Wireless Headphones",
  "description": "High-quality wireless headphones with noise cancellation.",
  "price": 89.99,
  "category": "Electronics",
  "image": "https://example.com/image.jpg"
}

Response:
201 Created

json

{
  "message": "Product created successfully",
  "product": {
    "_id": "60e6c1d18b456f0e74f6d3b5",
    "name": "Wireless Headphones",
    "description": "High-quality wireless headphones with noise cancellation.",
    "price": 89.99,
    "category": "Electronics",
    "image": "https://example.com/image.jpg",
    "createdAt": "2024-10-18T12:34:56.789Z",
    "updatedAt": "2024-10-18T12:34:56.789Z"
  }
}

*Update a Product*
- Endpoint: PUT /products/:id

- Updates an existing product by its ID.

Request Body:
json

{
  "name": "Updated Wireless Headphones",
  "description": "Updated description for wireless headphones.",
  "price": 79.99,
  "category": "Electronics",
  "image": "https://example.com/image-updated.jpg"
}

Response:
200 OK

json

{
  "message": "Product updated successfully",
  "product": {
    "_id": "60e6c1d18b456f0e74f6d3b5",
    "name": "Updated Wireless Headphones",
    "description": "Updated description for wireless headphones.",
    "price": 79.99,
    "category": "Electronics",
    "image": "https://example.com/image-updated.jpg",
    "createdAt": "2024-10-18T12:34:56.789Z",
    "updatedAt": "2024-10-18T12:34:56.789Z"
  }
}
`
*Delete a Product*
- Endpoint: DELETE /products/:id

- Deletes a product by its ID.

Response:
204 No Content

*Order Management*
- Create an Order
- Endpoint: POST /orders

- Creates a new order.

Request Body:
json

{
  "userId": "60e6c1d18b456f0e74f6d3b5",
  "products": [
    {
      "productId": "60e6c1d18b456f0e74f6d3b5",
      "quantity": 1
    },
    {
      "productId": "60e6c1d18b456f0e74f6d3b6",
      "quantity": 2
    }
  ],
  "totalAmount": 199.97
}

Response:
201 Created

json

{
  "message": "Order created successfully",
  "order": {
    "_id": "60e6c1d18b456f0e74f6d3b7",
    "userId": "60e6c1d18b456f0e74f6d3b5",
    "products": [
      {
        "productId": "60e6c1d18b456f0e74f6d3b5",
        "quantity": 1
      },
      {
        "productId": "60e6c1d18b456f0e74f6d3b6",
        "quantity": 2
      }
    ],
    "totalAmount": 199.97,
    "status": "Pending",
    "createdAt": "2024-10-18T12:34:56.789Z"
  }
}

**Get Orders by User*
- Endpoint: GET /orders/:userId

- Retrieves all orders for a specific user.

Response:
200 OK

json

[
  {
    "_id": "60e6c1d18b456f0e74f6d3b7",
    "userId": "60e6c1d18b456f0e74f6d3b5",
    "products": [
      {
        "productId": "60e6c1d18b456f0e74f6d3b5",
        "quantity": 1
      },
      {
        "productId": "60e6c1d18b456f0e74f6d3b6",
        "quantity": 2
      }
    ],
    "totalAmount": 199.97,
    "status": "Pending",
    "createdAt": "2024-10-18T12:34:56.789Z"
  }
]

*Get All Orders*
- Endpoint: GET /orders

- Retrieves a list of all orders.

Response:
200 OK

json

[
  {
    "_id": "60e6c1d18b456f0e74f6d3b7",
    "userId": "60e6c1d18b456f0e74f6d3b5",
    "products": [
      {
        "productId": "60e6c1d18b456f0e74f6d3b5",
        "quantity": 1
      },
      {
        "productId": "60e6c1d18b456f0e74f6d3b6",
        "quantity": 2
      }
    ],
    "totalAmount": 199.97,
    "status": "Pending",
    "createdAt": "2024-10-18T12:34:56.789Z"
  }
]

*Update Order Status*
- Endpoint: PUT /orders/:id

- Updates the status of an existing order.

Request Body:
json

{
  "status": "Shipped"
}
Response:
200 OK

json

{
  "message": "Order status updated successfully",
  "order": {
    "_id": "60e6c1d18b456f0e74f6d3b7",
    "userId": "60e6c1d18b456f0e74f6d3b5",
    "products": [
      {
        "productId": "60e6c1d18b456f0e74f6d3b5",
        "quantity": 1
      },
      {
        "productId": "60e6c1d18b456f0e74f6d3b6",
        "quantity": 2
      }
    ],
    "totalAmount": 199.97,
    "status": "Shipped",
    "createdAt": "2024-10-18T12:34:56.789Z"
  }
}

*Delete an Order*
- Endpoint: DELETE /orders/:id

- Deletes an order by its ID.


Response:
204 No Content

### Error Handling
The API uses standard HTTP status codes to indicate the success or failure of requests. The following are common error responses:

- 400 Bad Request: The request was invalid or cannot be served.
- 401 Unauthorized: Authentication failed or user does not have permissions for the requested operation.
- 404 Not Found: The requested resource could not be found.
- 500 Internal Server Error: An unexpected error occurred on the server.

# Rate Limiting
The Duka Moja API implements rate limiting to prevent abuse. Requests are limited to 100 per hour per user. If this limit is exceeded, a 429 Too Many Requests response will be returned.

##Contact Information
For any inquiries or support, please contact us at:

Email: wanjiku.kahira@gmail.com - sharon kahira
       moyiedwin8@gmail.com -   Edwin nga'nga
       moyiedwin8@gmail.com - Amos Olouch