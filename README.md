# Duka Platform API

This repository contains the backend implementation of an E-Commerce platform using Flask-restful and SQLAlchemy. The API supports user authentication, product management, order processing, and more.

## Table of Contents

- [Duka Platform API](#duka-platform-api)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Key Features](#key-features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Install dependencies:](#install-dependencies)
    - [Usage](#usage)
  - [*NOTE*](#note)
  - [API Endpoints](#api-endpoints)
    - [Users](#users)
    - [Products](#products)
    - [Orders](#orders)
  - [Running Tests](#running-tests)
  - [Contributing](#contributing)
  - [License](#license)
    - [Acknowledgements](#acknowledgements)
    - [Author](#author)

## Description

The Duka Platform API is designed to facilitate an online shopping experience by managing users, products, orders, and order items. This API handles various operations like user registration, login, product creation, and order processing.

## Key Features

- *User Authentication*: Users can register, log in, and manage their sessions securely.
- *Product Management*: Create, read, update, and delete products.
- *Order Processing*: Users can create orders and manage their order items.
- *Flexible Data Model*: Utilizes SQLAlchemy for ORM, enabling easy database interactions.
- *RESTful API*: Follows REST principles for seamless integration with frontend applications.

## Prerequisites

Ensure you have the following installed:

- *Python 3.7 or later*: Download from [python.org](https://www.python.org/downloads/).
- *PostgreSQL*: Download and install from [postgresql.org](https://www.postgresql.org/download/).
- *pip*: Package installer for Python (comes with Python installation).
- *Flask*
- *Flask-restful*
- *Flask-migrate*
- *Flask-sqlalchemy*

## Installation

To set up the project locally, follow these steps:

1. *Clone the repository*:
   git clone https://github.com/your-username/e-commerce-platform.git
   cd e-commerce-platform
2. Create a virtual environment:
- pipenv install && pipenv shell
- source venv/bin/activate  # On Windows use venv\Scripts\activate

## Install dependencies:
- pip install -r requirements.txt
- Set up the database:

1. Make sure your PostgreSQL server is running.
2. Create a database for the application:
   - sql
   - CREATE DATABASE dukadb;
3. Run migrations:

 - flask db init
 - flask db migrate
 - flask db upgrade
4. Start the application:
 - flask run
The API will be available at http://127.0.0.1:5000.

### Usage
The API provides various endpoints for interaction:

- *User Registration*: POST /register
- *User Login*: POST /login
- *Get All Users*: GET /users
- *Get User by ID*: GET /users/<id>
- *Create Product*: POST /products
- *Get All Products*: GET /products
- *Get Product by ID*: GET /products/<id>
- *Create Order*: POST /orders
- *Get All Orders*: GET /orders
- *Get Order by ID*: GET /orders/<id>

 ## *NOTE*
 *IDs are not from 1 refer to database
 
- Refer to the API Endpoints section for detailed usage instructions.

## API Endpoints
### Users
POST /register

Request Body: {"name": "string", "email": "string", "password": "string"}
Response: Newly created user object.

POST /login

Request Body: {"email": "string", "password": "string"}
Response: User information and session status.

### Products
GET /products

Response: List of all products.

POST /products

Request Body: {"name": "string", "description": "string", "price": "float", "image": "string"}
Response: Newly created product object.

### Orders
POST /orders
Request Body: {"user_id": "integer", "address": "string", "status": "string"}
Response: Newly created order object.
## Running Tests
To run the tests for this project, ensure your virtual environment is activated and execute:
- POSTMAN or port=5000
## Contributing
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
3. git checkout -b feature/YourFeature
4. Make your changes and commit them:
 - git commit -m "Add a new feature"
 - Push to your branch:
 - git push origin feature/YourFeature
 - Create a pull request.
## License
This project is licensed under the MIT License. See the LICENSE file for more details.

Credits
This project was developed by Edwin,Amos,Sharon,Vincent,John. Special thanks to the following libraries and tools:

- Flask
- SQLAlchemy
- Flask-Restful
- Flask-Migrate
### Acknowledgements
Thanks to the Flask community for their extensive documentation and support.
Additional thanks to tutorials and resources that guided the development process.

### Author

[Sharon Kahira](https://github.com/Her-Code)
[Vincent Irungu](https://github.com/Phoenixvince)
[Edwin Ng'anga](https://github.com/Programer-Ed)
[Amos Oluoch](https://github.com/aulouch)
[John Muchiri](https://github.com/MUCHIRIJOHN1990)