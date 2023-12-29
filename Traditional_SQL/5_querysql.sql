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
