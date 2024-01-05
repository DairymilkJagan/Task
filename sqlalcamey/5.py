from sqlalchemy import create_engine, Column, Integer, ForeignKey, func,VARCHAR
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Create an SQLAlchemy engine
engine = create_engine('postgresql+psycopg2://postgres:Jagansri%404217@localhost/sqltask5')

# Create an SQLAlchemy base class
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'
    emp_id = Column(Integer, primary_key=True)
    emp_fname = Column(VARCHAR(255))
    emp_lname = Column(VARCHAR(255))
    emp_dept = Column(Integer, ForeignKey('department.dpt_code'))
    department = relationship('Department')
class Department(Base):
    __tablename__ = 'department'
    dpt_code = Column(Integer, primary_key=True)
    dpt_name = Column(VARCHAR(255))
    dpt_allotment = Column(Integer)

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# First Query
query1_result = (
    session.query(Employee.emp_fname, Employee.emp_lname)
    .join(Department, Employee.emp_dept == Department.dpt_code)
    .filter(Department.dpt_allotment > 50000)
    .all()
)

# Print the result of the first query
print("\n query 1 result:\n")
for row in query1_result:
    print(row)

# Second Query
subquery = (
    session.query(Department.dpt_code, func.min(Department.dpt_allotment).label('min_allotment'))
    .group_by(Department.dpt_code)
    .order_by(func.min(Department.dpt_allotment))
    .limit(1).offset(1)  # Skip the lowest and take the second lowest
    .subquery()
)

query2_result = (
    session.query(Employee.emp_fname, Employee.emp_lname)
    .join(subquery, Employee.emp_dept == subquery.c.dpt_code)
    .all()
)

# Print the result of the second query
print("\n query 2 result:\n")
for row in query2_result:
    print(row)
