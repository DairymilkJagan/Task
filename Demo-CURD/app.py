from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from functools import wraps

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Jagansri%404217@localhost/task'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def handle_exceptions(route_function):
    @wraps(route_function)
    def decorated_function(*args, **kwargs):
        try:
            return route_function(*args, **kwargs)
        except SQLAlchemyError as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

    return decorated_function

class Employee(db.Model):
    __tablename__ = "employee"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Float, nullable=False)

# Create tables
db.create_all()

# GET all employees
@app.route('/employees', methods=['GET'])
@handle_exceptions
def get_employees():
    employees = Employee.query.all()
    employee_list = []
    for employee in employees:
        employee_data = {
            'id': employee.id,
            'first_name': employee.first_name,
            'last_name': employee.last_name,
            'email': employee.email,
            'department': employee.department,
            'salary': employee.salary
        }
        employee_list.append(employee_data)
    return render_template('employees.html', employee_list=employee_list)

# GET single employee by ID
@app.route('/employees/<int:id>', methods=['GET'])
@handle_exceptions
def get_employee(id):
    employee = Employee.query.get(id)
    if employee:
        employee_data = {
            'id': employee.id,
            'first_name': employee.first_name,
            'last_name': employee.last_name,
            'email': employee.email,
            'department': employee.department,
            'salary': employee.salary
        }
        return jsonify({'employee': employee_data})
    else:
        return jsonify({'message': 'Employee not found'}), 404

# POST to add a new employee
@app.route('/employees', methods=['POST'])
@handle_exceptions
def add_employee():
    data = request.form.to_dict()
    new_employee = Employee(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        department=data['department'],
        salary=data['salary']
    )
    db.session.add(new_employee)
    db.session.commit()
    return redirect(url_for('get_employees'))

@app.route('/delete', methods=["POST"])
@handle_exceptions
def delete_employee():
    delete_values_id = request.form.get('id')
    delete_values_email = request.form.get('email')

    if delete_values_id is None or delete_values_email is None:
        return jsonify({'error': 'Both parameters (id and email) are required.'}), 400

    employee_to_delete = (
        Employee.query.filter(
            (Employee.id == delete_values_id) &
            (Employee.email == delete_values_email)
        ).first()
    )

    if employee_to_delete is None:
        return jsonify({'message': 'Employee not found'}), 404

    db.session.delete(employee_to_delete)
    db.session.commit()
    return redirect(url_for('get_employees'))


@app.route('/update_employee', methods=["POST"])
@handle_exceptions
def update_employee():
        print("123")
        form_data = request.form.to_dict() 
        employee_id  = form_data['id']
        employee = Employee.query.get(employee_id)
        
        employee_values= {
               'id': employee.id,
                'first_name': employee.first_name,
                'last_name': employee.last_name,
                'email': employee.email,
                'department': employee.department,
                'salary': float(employee.salary)
        }
        if not employee:
            return jsonify({'message': 'Employee not found'}), 404
        else:
            print("test...")
            for key, value in employee_values.items():
              if key not in form_data:
                 form_data[key] = value
        print(form_data)
        db.session.commit()      
        return "Data update successfully"

# @app.route('/update_employees', methods=["PUT"])
# @handle_exceptions
# def update_employee():
#     form_data = request.form.to_dict() 
#     employee_id = form_data.get('id')

#     if not employee_id:
#         return jsonify({'error': 'ID is required for updating an employee'}), 400

#     employee = Employee.query.get(employee_id)

#     if not employee:
#         return jsonify({'message': 'Employee not found'}), 404

#     # Update employee attributes
#     employee.first_name = form_data.get('first_name', employee.first_name)
#     employee.last_name = form_data.get('last_name', employee.last_name)
#     employee.email = form_data.get('email', employee.email)
#     employee.department = form_data.get('department', employee.department)
#     employee.salary = form_data.get('salary', employee.salary)

#     db.session.commit()      
#     return redirect(url_for('get_employees'))

if __name__ == "__main__":
    app.run()
