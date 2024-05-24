from flask import Blueprint, request, jsonify
from .models import Employee
from app.database import db
from .utils import validate_data, call_api
from datetime import datetime

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/', methods = ['GET'])
def home():
    return jsonify({"message": "Welcome to SMS-MAGIC Assignment!"})


@employee_bp.route('/employee', methods = ['POST'])
def add_employee():
    try:
        data = request.json
        if not validate_data(data):
            return jsonify({"error": "Invalid Data"}), 400

        response = call_api(data)
        if response.status_code != 201:
            return jsonify({"error": "API request failed"}), 500  

        response_data = response.json()

        ext_id = response_data.get('id')
        created_at = datetime.fromisoformat(response_data.get('createdAt').rstrip('Z'))

        new_employee = Employee(
            name = data['name'],
            email = data['email'],
            position = data['position'],
            salary = data['salary'],
            ext_id = ext_id,
            created_at = created_at
        )

        db.session.add(new_employee)
        db.session.commit()

        return jsonify({"message": "Employee added",
                "employee": {
                    'id': new_employee.id,
                    'name': new_employee.name,
                    'email': new_employee.email,
                    'position': new_employee.position,
                    'salary': new_employee.salary,
                    'ext_id': new_employee.ext_id,
                    'created_at': new_employee.created_at
                }
        }), 201
    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify({"error": str(e)}), 500

@employee_bp.route('/employees', methods=['GET'])
def get_all_employees():
    try:
        employees = Employee.query.all()
        employee_list = []
        for emp in employees:
            employee_data = {
                    'id': emp.id,
                    'name': emp.name,
                    'email': emp.email,
                    'position': emp.position,
                    'salary': emp.salary,
                    'ext_id': emp.ext_id,
                    'created_at': emp.created_at
            }
            employee_list.append(employee_data)
        return jsonify(employee_list), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@employee_bp.route('/employee/<int:id>', methods = ['GET'])
def get_employee(id):
    try:
        employee = Employee.query.get_or_404(id)
    
        return jsonify({
            'id': employee.id,
            'name': employee.name,
            'email': employee.email,
            'position': employee.position,
            'salary': employee.salary,
            'ext_id': employee.ext_id,
            'created_at': employee.created_at,
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@employee_bp.route('/employee/<int:id>', methods = ['PUT'])
def update_employee(id):
    try:
        data = request.json
        if not validate_data(data):
            return jsonify({"error": "Invalid data"}), 400
        
        employee = Employee.query.get_or_404(id)

        employee.name = data['name']
        employee.email = data['email']
        employee.position = data['position']
        employee.salary = data['salary']
        db.session.commit()
        
        return jsonify({"message": "Employee updated"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@employee_bp.route('/employee/<int:id>', methods = ['DELETE'])
def delete_employee(id):
    try:
        employee = Employee.query.get_or_404(id)
        
        db.session.delete(employee)
        db.session.commit()

        return jsonify({"message": "Employee successfully deleted"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500