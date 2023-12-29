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