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