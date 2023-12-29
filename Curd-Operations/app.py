from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask import Flask, render_template, jsonify, request ,redirect,url_for
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
@app.route("/")
def home():
    return "Hello World !, I am Jagan"
# Explore how to connect postgres DB with flask app in local.

def get_db_connection():
    conn = psycopg2.connect(host= 'localhost',
                            database = "pg_database",
                            port ="5432",
                            user = "postgres",
                            password = "Jagansri@4217")
    return conn

@app.route('/psql')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM teams;')
    teams = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', teams=teams)

# Write a simple flask API with 
# GET method with 2 parameters 
# A and B and return their sum as result local browser.

@app.route('/add', methods=['GET'])
def add_numbers():
    return render_template('add.html')


@app.route('/add', methods=['POST'])
def add_numbers1():
    # Get the values of 'a' and 'b' from the query parameters
    a = request.form.get('a')
    b = request.form.get('b')

    # Check if both parameters are provided
    if a is None or b is None:
        return jsonify({'error': 'Both parameters (a and b) are required.'}), 400
    
    # Calculate the sum
    result = int(a) + int(b)

    # Return the result as JSON
    return  str(result)

#  Write a simple flask API with POST method that computes the net amount of a bank account.
#  Based on input transaction mode print current amount present in bank balance

@app.route('/bank', methods=['GET'])
def bank_transaction():
    return render_template('bank.html')

@app.route('/bank', methods=['POST'])
def bank_transaction1():

    # Get given data from the request
    a = request.form.get('net_amount')
    b = request.form.get('mode')
    c = request.form.get('amount')

    # print = a,b,c

    # Validate required fields in the data
    # if not all(key in data for key in ['net_amount', 'mode', 'amount']):
    # return jsonify({'error': 'Invalid input. Missing required fields.'}), 400

    # convey the value of integers
    net_amount = int (a)
    transaction_mode = b
    transaction_amount = int (c)

    # Perform the transaction based on the mode (deposit or withdraw)
    if transaction_mode == 'deposit':
        net_amount += transaction_amount
    elif transaction_mode == 'withdraw':
        net_amount -= transaction_amount
    else:
        return jsonify({'error': 'Invalid transaction mode. Use "deposit" or "withdraw".'}), 400

    # Return the current net amount after the transaction
    return str(net_amount)

    # app.run(debug=True)

#  Write simple GET, POST , PUT, DELETE API’s 
# ( To add employee details, get employee details, update emp details, delete employee details). 
# Connect your flask app with local postgres DB using Flask and SQLAlchemy.
    
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Jagansri%404217@localhost/task'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee(db.Model):
    __tablename__ = "employee"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Float, nullable=False)

#  Create tables
db.create_all()

#  GET all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    try:
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
        return render_template('employees.html',employee_list = employee_list)
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# GET single employee by ID
@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    try:
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
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# POST to add a new employee
@app.route('/employees', methods=['POST'])
def add_employee():
    try:
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
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# DELETE employee by ID
@app.route('/delete', methods=['POST'])
def delete_employee():
    try:
        employee = request.form.get('id')
        details = Employee.query.filter(Employee.id == str(employee)).first()
        # details = Employee.query.filter(Employee.id == str(employee))
        # print("Employee ID to delete:", employee)
        if details:
            db.session.delete(details)
            db.session.commit()
            return redirect(url_for('get_employees'))
        else:
            return jsonify({'message': 'Employee not found'}), 404
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    
@app.route('/update_employee', methods=["GET"])
def update_employee():
        form_data = request.form.to_dict() 
        employee_id  = form_data['id']
        employee = Employee.query.get(employee_id)
        
        employee_values= {
               'id': employee.employee_id,
                'first_name': employee.first_name,
                'last_name': employee.last_name,
                'email': employee.email,
                'department': employee.department,
                'salary': float(employee.salary)
        }
        if not employee:
            return jsonify({'message': 'Employee not found'}), 404
        else:
            for key, value in employee_values.items():
              if key not in form_data:
                 form_data[key] = value
        print(form_data)
        db.session.commit()      
        return "Data update successfully"


if __name__ == '__main__':
    app.run(debug=True)