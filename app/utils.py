import requests

def validate_data(data):
    required_fields = ['name', 'email', 'position', 'salary']
    for field in required_fields:
        if field not in data:
            return False
    return True

def call_api(employee_data):
    url = "https://reqres.in/api/users"
    emp_data = {
        "name": employee_data['name'],
        "job": employee_data['position'],
        "email": employee_data['email'],
        "salary": employee_data["salary"]
    }
    response = requests.post(url, json=emp_data)
    
    return response