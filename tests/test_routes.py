import json

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Welcome to SMS-MAGIC Assignment!"}

def test_add_employee(client, init_database):
    employee_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "position": "Software Engineer",
        "salary": 50000.0
    }
    response = client.post('/employee', data=json.dumps(employee_data), content_type='application/json')
    assert response.status_code == 201
    assert response.json['message'] == "Employee added"
    assert response.json['employee']['name'] == "John Doe"
    assert response.json['employee']['email'] == "john@example.com"
    assert response.json['employee']['position'] == "Software Engineer"
    assert response.json['employee']['salary'] == 50000.0

    invalid_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "position": "Software Engineer"
    }
    response = client.post('/employee', data=json.dumps(invalid_data), content_type='application/json')
    assert response.status_code == 400
    assert response.json == {"error": "Invalid Data"}

def test_get_all_employees(client, init_database):
    response = client.get('/employees')
    assert response.status_code == 200
    assert response.json == []

    employee_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "position": "Software Engineer",
        "salary": 50000.0
    }
    client.post('/employee', data=json.dumps(employee_data), content_type='application/json')

    response = client.get('/employees')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['name'] == "John Doe"
    assert response.json[0]['email'] == "john@example.com"
    assert response.json[0]['position'] == "Software Engineer"
    assert response.json[0]['salary'] == 50000.0

def test_get_employee(client, init_database):
    employee_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "position": "Software Engineer",
        "salary": 50000.0
    }
    response = client.post('/employee', data=json.dumps(employee_data), content_type='application/json')
    employee_id = response.json['employee']['id']

    response = client.get(f'/employee/{employee_id}')
    assert response.status_code == 200
    assert response.json['name'] == "John Doe"
    assert response.json['email'] == "john@example.com"
    assert response.json['position'] == "Software Engineer"
    assert response.json['salary'] == 50000.0

def test_update_employee(client, init_database):
    employee_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "position": "Software Engineer",
        "salary": 50000.0
    }
    response = client.post('/employee', data=json.dumps(employee_data), content_type='application/json')
    employee_id = response.json['employee']['id']

    updated_data = {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "position": "Senior Software Engineer",
        "salary": 60000.0
    }
    response = client.put(f'/employee/{employee_id}', data=json.dumps(updated_data), content_type='application/json')
    assert response.status_code == 200
    assert response.json['message'] == "Employee updated"

    response = client.get(f'/employee/{employee_id}')
    assert response.status_code == 200
    assert response.json['name'] == "Jane Doe"
    assert response.json['email'] == "jane@example.com"
    assert response.json['position'] == "Senior Software Engineer"
    assert response.json['salary'] == 60000.0

def test_delete_employee(client, init_database):
    employee_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "position": "Software Engineer",
        "salary": 50000.0
    }
    response = client.post('/employee', data=json.dumps(employee_data), content_type='application/json')
    employee_id = response.json['employee']['id']

    response = client.delete(f'/employee/{employee_id}')
    assert response.status_code == 200
    assert response.json['message'] == "Employee successfully deleted"

    response = client.get(f'/employee/{employee_id}')
    assert response.status_code == 404
    assert response.json == {"error": "Employee not found"}