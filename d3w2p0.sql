CREATE DATABASE w2d3am;
-- Create the students table

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INTEGER,
    campus_id INTEGER,
    total_grade FLOAT
);

-- Insert data into the students table
INSERT INTO students (name, age, campus_id, total_grade)
VALUES
    ('Rafif Iman', 20, 1, 85.5),
    ('Hana Arisona', 21, 2, 90.2),
    ('Raka Purnomo', 19, 1, 78.9),
    ('Danu Irfansyah', 20, 3, 92.7),
    ('Rachman Ardhi', 22, 2, 88.1);

-- Create the campus table
CREATE TABLE campus (
    id SERIAL PRIMARY KEY,
    campus_name VARCHAR(50),
    batch VARCHAR(10),
    start_date DATE
);

-- Insert data into the campus table
INSERT INTO campus (campus_name, batch, start_date)
VALUES
    ('Remote', 'RMT-1', '2023-01-01'),
    ('Jakarta', 'HCK-2', '2023-02-01'),
    ('BSD', 'BSD-4', '2023-03-01'),
    ('Surabaya', 'SUB-1', '2023-04-01'),
    ('Singapore', 'SIN-1', '2023-05-01');

--Data Query Language

--Select
--Scenario 1 (All Columns)
select * from students;
--Scenario 2 (Selected Columns)
select name, total_grade from students;

--Select Distinct
SELECT DISTINCT campus_id FROM students;

--Alias
--Cara 1 Pake AS
SELECT name AS full_name
	FROM students;
--Cara 2 Pake spasi , GAPAKE AS
SELECT name full_name
	FROM students;
-- Where -- 
-- = 		equal to 
-- != 		or <> not equal
-- > 		greater than
-- < 		less than
-- >= 		greater than or equal to 
-- <= 		less than or equal to
-- BETWEEN 	within range
-- IN 		match set of values
-- LIKE 	match pattern (case sensitive)
-- ILIKE 	match pattern (case insensitive)
	-- Wildcards
	-- _ 	represent single character
	-- % 	represent one or more character
--NOT 		negates a condition

SELECT 
	name,
	total_grade
FROM students
WHERE total_grade > 90;

SELECT 
	name,
	total_grade
from students 
WHERE total_grade BETWEEN 70 AND 80;

--student age 19 20 and 200

SELECT 
	name,
	age
FROM students
WHERE age NOT IN (19, 20 , 22);
-- Filter Students name that start with "R"
SELECT name AS full_name
FROM students
WHERE name LIKE 'R%'
	--ILIKE
SELECT name AS full_name
FROM students
WHERE name ILIKE 'r%';

-- Filter students name start with R and char length is 10
SELECT name AS full_name 
FROM students
WHERE NAME LIKE 'R_____';
-- Filter students name that ends with "omo"
SELECT name AS full_name
FROM students 
WHERE name ILIKE '%omo';
-- Filter students name that has second and third char is "an"
SELECT name AS full_name
FROM students 
WHERE name ILIKE '_an%';

-- And / Or --  
-- And a condition and both/all have to be True
-- Filter Students 
SELECT * 
FROM students 
WHERE age = 20 AND campus_id = 1;

--filter stuedents that age less or equal to 20 and total grade greater than 80

SELECT *
FROM students
WHERE age <= 20 AND total_grade >80;

-- or add conditions and at least one of them have to be true
-- Filter 
Select *
FROM students 
WHERE name LIKE 'D%' OR name LIKE 'R%';

-- Combine 
-- Filter Students name that starts with D / H in pondok indah campus 
SELECT * 
FROM students 
WHERE campus_id = 2 AND name LIKE 'D%' or name LIKE 'H%';

-- PERBESAR USAHA PERKECIL GAYA , MAKANYA JANGAN BANYAK GAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

-- Order By --
-- Ascending
SELECT NAME AS full_name 
FROM students
ORDER BY name;
SELECT NAME AS full_name 
FROM students
ORDER BY name ASC;

-- Descending
SELECT name, total_grade
FROM students 
ORDER BY total_grade DESC;

--Group by & Aggregation
SELECT 
	campus_id,
	COUNT(name) AS "students_count",				-- TO KNOW HOW MANY STUDENTS IN EACH CAMPUS 
	SUM(total_grade) AS "sum_of_grade,",  		--TO KNOW SUMMARY OF GRADE IN EACH CAMPUS 
	AVG(total_grade) AS "average_grade" ,		--TO KNOW AVERAGE OF GRADE IN EACH CAMPUS
	MIN(total_grade) AS "minimum_grade" ,		--TO KNOW MINIMUM OF GRADE IN EACH CAMPUS 
	MAX(total_grade) AS "maximum grade" 		--TO KNOW MAXIMUM OF GRADE IN EACH CAMPUS 
	
FROM students
GROUP BY campus_id;


--HAVING -- 
-- Condition that can contain Aggregation
-- Filter Average grade in BSD CAMPUS
SELECT
	campus_id,
	AVG(total_grade)
FROM students
GROUP BY campus_id
HAVING campus_id = 3;

-- Join -- 
-- Inner Join (Hanya menampilkan yang match pada semua table )
SELECT 
	country.*,
	city.*
FROM country 			
JOIN city ON country.id = city.country_id;
-- Full Join 
SELECT 
	co.country_name,
	ci.city_name,
	ci.country_id
FROM country AS co 
FULL JOIN city AS ci ON co.id = ci.country_id

SELECT *
FROM

	(SELECT 
	co.country_name,
	ci.city_name,
	ci.country_id
FROM country AS co 
FULL JOIN city AS ci ON co.id = ci.country_id) AS subquery
WHERE subquery.city_name IS NOT NULL AND subquery.country_name IS NOT NULL;

-- Left Join (Memprioritaskan table yang dipanggil duluan atau setelah FROM)
SELECT
	ci.city_name,
	ci.country_id,
	co.country_name
from country AS co -- Left Table 
LEFT JOIN city AS ci -- Right table
	ON co.id = ci.country_id;

-- Right Join
SELECT
	ci.city_name,
	ci.country_id,
	co.country_name
from country AS co -- Left Table 
RIGHT JOIN city AS ci -- Right table
	ON co.id = ci.country_id;
-- Right Join (Mempiroritaskan table yang dipanggil belakangan atau setelah JOIN)


SELECT * FROM campus;
SELECT * FROM students;

CREATE TABLE country();

CREATE TABLE city();