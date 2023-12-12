-- Create the database
CREATE DATABASE IF NOT EXISTS company;

-- Use the database
USE company;

-- Create the employees table with DATETIME data type
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(255),
    start_time DATETIME,
    end_time DATETIME
);

-- Insert some sample data with the specified date and time format
INSERT INTO employees (employee_id, employee_name, start_time, end_time)
VALUES
    (1, 'John Doe', '2023-11-02T08:00:00.000Z', '2023-11-02T17:00:00.000Z'),
    (2, 'Jane Smith', '2023-11-02T09:00:00.000Z', '2023-11-02T18:00:00.000Z'),
    (3, 'Bob Johnson', '2023-11-02T08:30:00.000Z', '2023-11-02T16:30:00.000Z');

SELECT * FROM employees;
-- calculate working hours
SELECT 
    employee_id, 
    employee_name,
    TIMEDIFF(end_time, start_time) AS total_working_hours
FROM employees;
