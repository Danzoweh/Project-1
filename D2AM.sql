-- DDL
-- creating database
CREATE DATABASE FTDS;

-- create student table
CREATE TABLE students(
	id SERIAL PRIMARY KEY ,
	name VARCHAR(50) ,
	age INTEGER , 
	campus_id INTEGER, 
	total_grade FLOAT
);

-- create campus table 
CREATE TABLE campus (
	id SERIAL PRIMARY KEY,
	campus_name VARCHAR(50),
	batch VARCHAR(10),
	start_date DATE
);


-- check tabel
SELECT * FROM campus; 
SELECT * FROM students;

-- DML
-- Insert the data
INSERT INTO students (name, age, campus_id, total_grade)
VALUES 
	('Rafif Iman', 20 , 1 , 85.5),
	('Hana Arisona', 21, 2, 90.2),
	('Raka Purnomo', 19, 1, 78.9),
	('Danu Irfansyah', 20, 3, 92.7),
	('Rachman Ardhi', 22, 2, 88.1);

-- Insert data campus
INSERT INTO campus(campus_name, batch, start_date)
VALUES
	('Malang', 'MLG-1','2023-01-01'),
	('Jakarta', 'HCK-2', '2023-02-01'),
	('BSD', 'BSD-4', '2023-03-01'),
	('Surabaya', 'SBY-1', '2023-04-01'),
	('Singapore','SIN-1', '2023-05-01');

-- UPDATE, set new value
UPDATE students
SET total_grade = 95.3
WHERE id=15;

SELECT * FROM students;

--DELETE, remove a row 
DELETE FROM campus 
WHERE id=5;

-- check 
SELECT * FROM students 

--ALTER
--ALTER COLUMN
ALTER TABLE students
ADD COLUMN email VARCHAR(70);

-- ALTER RENAME COLUMN 
ALTER TABLE campus 
RENAME COLUMN campus_name TO name;

SELECT * FROM campus;

-- TRUNCATE 
TRUNCATE TABLE campus;

-- DROP
DROP TABLE campus;

--DROP on column
ALTER TABLE students 
DROP COLUMN email;

SELECT * FROM students
WHERE id IN (11, 12, 14);
