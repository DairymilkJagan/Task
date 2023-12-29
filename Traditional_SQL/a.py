from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Jagansri%404217@localhost/task'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Order(db.Model):
    __tablename__ = 'orders'

    ord_no = db.Column(db.Integer, primary_key=True)
    purch_amt = db.Column(db.Float)
    ord_date = db.Column(db.String)
    customer_id = db.Column(db.Integer)
    salesman_id = db.Column(db.Integer, db.ForeignKey('salesmen.salesman_id'))
    salesman = db.relationship('Salesman', back_populates='orders')

class Salesman(db.Model):
    __tablename__ = 'salesmen'

    salesman_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    orders = db.relationship('Order', back_populates='salesman')

# Add the following line to create the tables before running queries
# db.create_all()
