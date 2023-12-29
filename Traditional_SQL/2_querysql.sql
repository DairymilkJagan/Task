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
