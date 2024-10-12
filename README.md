# Superheroes API

Welcome to the **Superheroes API**! This is a RESTful API that allows you to manage superheroes, their powers, and the relationships between them. Built with Flask, SQLAlchemy, and Flask-Migrate, this project provides a robust backend for your superhero-themed applications.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Migration](#database-migration)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- Create, read, update, and delete superheroes.
- Manage superhero powers.
- Establish relationships between superheroes and their powers.
- Supports CORS for cross-origin requests.
- Built-in database migration support with Flask-Migrate.

## Technologies

- **Python 3.12**
- **Flask**: A lightweight WSGI web application framework.
- **Flask-SQLAlchemy**: A SQLAlchemy extension for Flask applications.
- **Flask-Migrate**: Database migration handling for Flask applications using Alembic.
- **Flask-RESTful**: An extension for Flask that adds support for quickly building REST APIs.
- **Flask-CORS**: A Flask extension for handling Cross-Origin Resource Sharing (CORS).
- **SQLite**: The default database (can be configured to use other databases).

## Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package installer)

### Steps

1. Clone this repository:

   ```bash
   git clone https://github.com/Freddie1056/Superheroes-API.git
   cd Superheroes-API

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate
    For Windows:
    python -m venv venv
    venv\Scripts\activate

3. Install the required packages:


4. pip install -r requirements.txt
 Usage
 Set environment variables:


export FLASK_APP=app.py
export FLASK_ENV=development
For Windows:


set FLASK_APP=app.py
set FLASK_ENV=development
Run the application:


5. flask run
The API will be available at http://127.0.0.1:5555.

### API Endpoints
Heroes
GET /heroes - Retrieve a list of all heroes.
POST /heroes - Create a new hero.
GET /heroes/<id> - Retrieve a specific hero by ID.
PUT /heroes/<id> - Update a hero by ID.
DELETE /heroes/<id> - Delete a hero by ID.
Powers
GET /powers - Retrieve a list of all powers.
POST /powers - Create a new power.
GET /powers/<id> - Retrieve a specific power by ID.
PUT /powers/<id> - Update a power by ID.
DELETE /powers/<id> - Delete a power by ID.
Hero Powers
GET /hero_powers - Retrieve a list of all hero-power associations.
POST /hero_powers - Create a new hero-power association.
GET /hero_powers/<id> - Retrieve a specific hero-power association by ID.
PUT /hero_powers/<id> - Update a hero-power association by ID.
DELETE /hero_powers/<id> - Delete a hero-power association by ID.
Database Migration
To initialize and apply database migrations, run the following commands:

7. Initialize migration environment:

    ```bash

 flask db init
 Create a migration script:

   ```bash
flask db migrate -m "Initial migration."
Apply the migration:

   ```bash

flask db upgrade

## Testing
To run tests for this project, ensure you have all necessary packages installed, then execute the following command:


## pytest
Make sure you have pytest listed in your requirements.txt. You can add it by running:

  ```bash
pip install pytest
Contributing
Contributions are welcome! Please follow these steps:

## Fork the repository.
Create a new branch (git checkout -b feature/YourFeature).
Make your changes and commit them (git commit -m 'Add new feature').
Push to the branch (git push origin feature/YourFeature).
Create a pull request.



## License

This project is licensed under the MIT License - see the LICENSE.md file for details.