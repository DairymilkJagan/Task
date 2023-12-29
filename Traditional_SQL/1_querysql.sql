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

a) SELECT salesman_id, MAX(purch_amt) AS max_purchase
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
