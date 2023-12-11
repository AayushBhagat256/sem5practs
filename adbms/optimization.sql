create database college;
use college;

-- Create Students Table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(255),
    course_id INT
);

-- Create Courses Table
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(255)
);

-- Insert Sample Data into Students Table
INSERT INTO students VALUES (1, 'John Doe', 101);
INSERT INTO students VALUES (2, 'Jane Smith', 102);
INSERT INTO students VALUES (3, 'Bob Johnson', 101);
INSERT INTO students VALUES (4, 'Alice Brown', 103);

-- Insert Sample Data into Courses Table
INSERT INTO courses VALUES (101, 'Mathematics');
INSERT INTO courses VALUES (102, 'History');
INSERT INTO courses VALUES (103, 'Physics');

select * from students;
select * from courses;
-- nested queries
select student_id,student_name
from students
where course_id = (
select course_id from courses where course_name = 'Mathematics'
);
-- join queries
-- to get student name and corresponding courses name
select students.student_id, students.student_name, courses.course_name
from students
inner join courses on  students.course_id = courses.course_id ;

-- Left Join to get all students and their corresponding course names (including students without courses)
SELECT students.student_id, students.student_name, courses.course_name
FROM students
LEFT JOIN courses ON students.course_id = courses.course_id;

create index idx_courseId on students(course_id);
-- because join mai course_id use ho raha hai and voh fk hai 
select students.student_id, students.student_name, courses.course_name
from students
inner join courses on  students.course_id = courses.course_id ;

-- you can even use OPTIMIZE TABLE students, courses;





