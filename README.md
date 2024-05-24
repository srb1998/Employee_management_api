# Employee Management API

This is a Flask application that implements a RESTful API for managing employee records. The application supports adding, retrieving, updating, and deleting employees and integrates with an external API to fetch additional employee details.

## Requirements
- Python 3.8+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- requests

## Features

- Add a new employee
- Retrieve all employees
- Retrieve a specific employee by ID
- Update an employee's information
- Delete an employee
- Store employee data in an SQLite database

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
    ```
2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```
3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Set up the database:
    ```sh
    flask db init
    flask db migrate -m "First migration"
    flask db upgrade
    ```

## Running the Application

1. Start the Flask development server:
    ```sh
    flask run
    ```

2. The API will be accessible at http://127.0.0.1:5000


## API Endpoints

### Welcome
- URL: `/`
- Method: `GET`
- Response:
```json
{"message": "Welcome to SMS-MAGIC Assignment!"}
``` 

### Add a New Employee

- URL: `/employee`
- Method: `POST`
- Request: 
```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "position": "Software Engineer",
    "salary": 50000
}
```
- Response:
```json
{
    "message": "Employee added",
    "employee": {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "position": "Software Engineer",
        "salary": 50000,
        "ext_id": "external_id",
        "created_at": "2022-01-01T00:00:00"
    }
}
```

### Retrieve All Employees

- URL: `/employees`
- Method: `GET`
- Response:
```json
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "john@gmail.com",
        "position": "Software Engineer",
        "salary": 50000,
        "ext_id": "167",
        "created_at": "2024-05-24T12:00:34"
    },
    {
        "id": 2,
        "name": "Sourabh Gupta",
        "email": "sourabh@gmail.com",
        "position": "Software Developer",
        "salary": 40000,
        "ext_id": "122",
        "created_at": "2024-05-24T01:00:00"
    }
]
```

### Retrieve a Specific Employee by ID

- URL: `/employee/1`
- Method: `GET`
- Response:
```json
    {
        "id": 1,
        "name": "John Doe",
        "email": "john@gmail.com",
        "position": "Software Engineer",
        "salary": 50000,
        "ext_id": "167",
        "created_at": "2024-05-24T12:00:34"
    
```

### Update an Employee's Information

- URL: `/employee/1`
- Method: `PUT` 
- Request:
```json
{
    "name": "Michel Doe",
    "email": "Michel@gmail.com",
    "position": "Software Engineer",
    "salary": 80000
}
```
- Response:
```json
{"message": "Employee updated"}
```


### Delete an Employee

- URL: `/employee/<id>`
- Method: `DELETE` 
- Response:
```json
{"message": "Employee successfully deleted"}
```

## Environment Variables

This application uses the following environment variables:

The `SECRET_KEY` is used in the `create_app` function in the `__init__.py` file

