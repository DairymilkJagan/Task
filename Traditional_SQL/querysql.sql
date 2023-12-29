1. a) Write a SQL query for the provided table to retrieve 
    the first five unique salespeople IDs in order 
    based on higher purchase amounts, where each 
    salesperson's purchase amount should not exceed 2000.

CREATE TABLE orders (
    ord_no INT PRIMARY KEY,
    purch_amt NUMERIC,
    ord_date DATE,
    customer_id INT,
    salesman_id INT
);

INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id)
VALUES
    (70001, 150.5, '2012-10-05', 3005, 5002),
    (70009, 270.65, '2012-09-10', 3001, 5005),
    (70002, 65.26, '2012-10-05', 3002, 5001),
    (70004, 110.5, '2012-08-17', 3009, 5003),
    (70007, 948.5, '2012-09-10', 3005, 5002),
    (70005, 2400.6, '2012-07-27', 3007, 5001),
    (70008, 5760, '2012-09-10', 3002, 5001),
    (70010, 1983.43, '2012-10-10', 3004, 5006),
    (70003, 2480.4, '2012-10-10', 3009, 5003),
    (70012, 250.45, '2012-06-27', 3008, 5002),
    (70011, 75.29, '2012-08-17', 3003, 5007),
    (70013, 3045.6, '2012-04-25', 3002, 5001);

a)  Write a SQL query for the provided table to retrieve 
    the first five unique salespeople IDs in order 
    based on higher purchase amounts, where each 
    salesperson's purchase amount should not exceed 2000.

SELECT salesman_id, MAX(purch_amt) AS max_purchase
FROM orders
WHERE purch_amt < 2000
GROUP BY salesman_id
ORDER BY  max_purchase DESC


LIMIT 5;

 salesman_id | max_purchase
-------------+--------------
        5001 |        65.26
        5002 |        948.5
        5003 |        110.5
        5005 |       270.65
        5006 |      1983.43

b)  Write a SQL query for the provided table to retrieve 
    the first five unique salespeople IDs in order based 
    on lower purchase amounts, where each salesperson's purchase amount should exceed 100.

SELECT salesman_id, MIN(purch_amt) AS min_purchase
FROM orders
WHERE purch_amt > 100
GROUP BY salesman_id
ORDER BY salesman_id
LIMIT 5;

 salesman_id | min_purchase
-------------+--------------
        5001 |       2400.6
        5002 |        150.5
        5003 |        110.5
        5005 |       270.65
        5006 |      1983.43



##########################################


2.  a) Write a SQL query for the given 
    table to retrieve details of salespeople with 
    commissions ranging from 0.10 to 0.12.(Begin and end values are included.) 
    Return salesman_id, name, city, and commission.


CREATE TABLE salesman (
    salesman_id INT PRIMARY KEY,
    name VARCHAR(255),
    city VARCHAR(255),
    commission FLOAT
);

INSERT INTO salesman (salesman_id, name, city, commission)
VALUES
    (5001, 'James Hoog', 'New York', 0.15),
    (5002, 'Nail Knite', 'Paris', 0.13),
    (5005, 'Pit Alex', 'London', 0.11),
    (5006, 'Mc Lyon', 'Paris', 0.14),
    (5007, 'Paul Adam', 'Rome', 0.13),
    (5003, 'Lauson Hen', 'San Jose', 0.12);

a)  Write a SQL query for the given 
    table to retrieve details of salespeople with 
    commissions ranging from 0.10 to 0.12.(Begin and end values are included.) 
    Return salesman_id, name, city, and commission. 

    SELECT salesman_id, name, city, commission
    FROM salesman
    WHERE commission BETWEEN 0.10 AND 0.12;

 salesman_id |    name    |   city   | commission
-------------+------------+----------+------------
        5005 | Pit Alex   | London   |       0.11
        5003 | Lauson Hen | San Jose |       0.12

b)  Write a SQL query for the given table to retrieve 
    avg details of commissions ranging from 0.12 to 0.14.(Begin and end values are included.)
    
    SELECT AVG(commission) AS avg_commission
    FROM salesman
    WHERE commission BETWEEN 0.12 AND 0.14;

 avg_commission
----------------
           0.13


########################################3

3.  From the following table, write a SQL query to find those employees who 
    worked more than or equal to  two jobs in the past. Return employee id. 

CREATE TABLE employee_history (
    employee_id INT,
    start_date DATE,
    end_date DATE,
    job_id VARCHAR(50),
    department_id INT
);


INSERT INTO employee_history (employee_id, start_date, end_date, job_id, department_id)
VALUES
    (102, '2001-01-13', '2006-07-24', 'IT_PROG', 60),
    (101, '1997-09-21', '2001-10-27', 'AC_ACCOUNT', 110),
    (101, '2001-10-28', '2005-03-15', 'AC_MGR', 110),
    (201, '2004-02-17', '2007-12-19', 'MK_REP', 20),
    (114, '2006-03-24', '2007-12-31', 'ST_CLERK', 50),
    (122, '2007-01-01', '2007-12-31', 'ST_CLERK', 50),
    (200, '1995-09-17', '2001-06-17', 'AD_ASST', 90),
    (176, '2006-03-24', '2006-12-31', 'SA_REP', 80),
    (176, '2007-01-01', '2007-12-31', 'SA_MAN', 80),
    (200, '2002-07-01', '2006-12-31', 'AC_ACCOUNT', 90);

Q)  From the following table, write a SQL query to find those employees who 
    worked more than or equal to  two jobs in the past. Return employee id.

SELECT employee_id
FROM employee_history
GROUP BY employee_id
HAVING COUNT(DISTINCT job_id) >= 2;

 employee_id
-------------
         101
         176
         200


###########################################

4. a) Write a SQL statement to generate a list of salesmen 
    who either serve one or more customers or have not joined any customer yet. 
    The customers may have placed one or more orders with an order amount equal to or exceeding 2000, 
    and they must have a grade. Alternatively, customers may not have placed any order 
    with the associated supplier.
    (Use joins) Return cust_name, cust city, grade, Salesman name, ord_no, ord_date, purch_amt


A Total of 3 tables are involved in this problem. Two tables were created in the previous problems. 
salesman from problem 2, 
orders from problem 1

Other table customer, create using the below queries

CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    cust_name VARCHAR(255),
    city VARCHAR(255),
    grade INT,
    salesman_id INT
);

INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id)
VALUES
    (3002, 'Nick Rimando', 'New York', 100, 5001),
    (3007, 'Brad Davis', 'New York', 200, 5001),
    (3005, 'Graham Zusi', 'California', 200, 5002),
    (3008, 'Julian Green', 'London', 300, 5002),
    (3004, 'Fabian Johnson', 'Paris', 300, 5006),
    (3009, 'Geoff Cameron', 'Berlin', 100, 5003),
    (3003, 'Jozy Altidor', 'Moscow', 200, 5007),
    (3001, 'Brad Guzan', 'London', NULL, 5005);


SELECT c.cust_name,c.city,c.grade,s.name,o.ord_no,o.ord_date,o.purch_amt
FROM customer c
LEFT JOIN orders o ON c.customer_id = o.customer_id
LEFT JOIN salesman s ON c.salesman_id = s.salesman_id
WHERE(o.purch_amt >= 2000 AND c.grade IS NOT NULL)
    OR(o.customer_id IS NULL AND c.grade IS NOT NULL);

   cust_name   |   city   | grade |    name    | ord_no |  ord_date  | purch_amt
---------------+----------+-------+------------+--------+------------+-----------
 Brad Davis    | New York |   200 | James Hoog |  70005 | 2012-07-27 |    2400.6
 Nick Rimando  | New York |   100 | James Hoog |  70008 | 2012-09-10 |      5760
 Geoff Cameron | Berlin   |   100 | Lauson Hen |  70003 | 2012-10-10 |    2480.4
 Nick Rimando  | New York |   100 | James Hoog |  70013 | 2012-04-25 |    3045.6

b) Write a SQL statement to generate a report with the customer name, city, order number, order date, 
and purchase amount for customers on the list who must have a grade and placed one or more orders. 
Additionally, include orders placed by customers who are neither on the list nor have a grade.(Use joins)

SELECT c.cust_name, c.city, o.ord_no, o.ord_date, o.purch_amt
FROM customer c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE (c.grade IS NOT NULL AND o.customer_id IS NOT NULL)
   OR (c.grade IS NULL AND o.customer_id IS NULL);

   cust_name    |    city    | ord_no |  ord_date  | purch_amt
----------------+------------+--------+------------+-----------
 Graham Zusi    | California |  70001 | 2012-10-05 |     150.5
 Nick Rimando   | New York   |  70002 | 2012-10-05 |     65.26
 Geoff Cameron  | Berlin     |  70004 | 2012-08-17 |     110.5
 Graham Zusi    | California |  70007 | 2012-09-10 |     948.5
 Brad Davis     | New York   |  70005 | 2012-07-27 |    2400.6
 Nick Rimando   | New York   |  70008 | 2012-09-10 |      5760
 Fabian Johnson | Paris      |  70010 | 2012-10-10 |   1983.43
 Geoff Cameron  | Berlin     |  70003 | 2012-10-10 |    2480.4
 Julian Green   | London     |  70012 | 2012-06-27 |    250.45
 Jozy Altidor   | Moscow     |  70011 | 2012-08-17 |     75.29
 Nick Rimando   | New York   |  70013 | 2012-04-25 |    3045.6


 ##########################################################

 5. a) ‘From the following tables write a SQL query 
    to find those employees who work for the department 
    where the departmental allotment amount is more than Rs. 50000. 
    Return emp_fname and emp_lname.

CREATE TABLE employee (
    emp_idno INT PRIMARY KEY,
    emp_fname VARCHAR(255),
    emp_lname VARCHAR(255),
    emp_dept INT
);

INSERT INTO employee (emp_idno, emp_fname, emp_lname, emp_dept)
VALUES
    (127323, 'Michale', 'Robbin', 57),
    (526689, 'Carlos', 'Snares', 63),
    (843795, 'Enric', 'Dosio', 57),
    (328717, 'Jhon', 'Snares', 63),
    (444527, 'Joseph', 'Dosni', 47),
    (659831, 'Zanifer', 'Emily', 47),
    (847674, 'Kuleswar', 'Sitaraman', 57),
    (748681, 'Henrey', 'Gabriel', 47),
    (555935, 'Alex', 'Manuel', 57),
    (539569, 'George', 'Mardy', 27),
    (733843, 'Mario', 'Saule', 63),
    (631548, 'Alan', 'Snappy', 27),
    (839139, 'Maria', 'Foster', 57);


CREATE TABLE department (
    dpt_code INT PRIMARY KEY,
    dpt_name VARCHAR(255),
    dpt_allotment INT
);

INSERT INTO department (dpt_code, dpt_name, dpt_allotment)
VALUES
    (57, 'IT', 65000),
    (63, 'Finance', 15000),
    (47, 'HR', 240000),
    (27, 'RD', 55000),
    (89, 'QC', 75000);


SELECT e.emp_fname, e.emp_lname
FROM employee e
JOIN department d ON e.emp_dept = d.dpt_code
WHERE d.dpt_allotment > 50000;

 emp_fname | emp_lname
-----------+-----------
 Michale   | Robbin
 Enric     | Dosio
 Joseph    | Dosni
 Zanifer   | Emily
 Kuleswar  | Sitaraman
 Henrey    | Gabriel
 Alex      | Manuel
 George    | Mardy
 Alan      | Snappy
 Maria     | Foster


b)  From the following tables write a SQL query 
    to find the departments with the second lowest sanction amount. 
    Return emp_fname and emp_lname.

SELECT e.emp_fname, e.emp_lname
FROM employee e
JOIN department d ON e.emp_dept = d.dpt_code
WHERE d.dpt_code IN (
    SELECT dpt_code
    FROM (
        SELECT dpt_code, RANK() OVER (ORDER BY dpt_allotment) as rnk
        FROM department
    ) ranked
    WHERE rnk = 2
);

 emp_fname | emp_lname
-----------+-----------
 George    | Mardy
 Alan      | Snappy

