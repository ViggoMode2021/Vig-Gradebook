CREATE TABLE students(
	id SERIAL PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	graduation_year INT NOT NULL,
	student_id INT NOT NULL UNIQUE);

INSERT INTO students(first_name, last_name, graduation_year, student_id)
VALUES ('Bill', 'Burr', 2025, 12);

CREATE TABLE teachers(
	id SERIAL PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	subjects TEXT NOT NULL,
	class_1 TEXT NOT NULL UNIQUE,
	class_2 TEXT NOT NULL UNIQUE,
	class_3 TEXT NOT NULL UNIQUE,
	class_4 TEXT NOT NULL UNIQUE,
	class_5 TEXT NOT NULL UNIQUE);

INSERT INTO teachers(first_name, last_name, subjects, class_1, class_2, class_3, class_4, class_5)
VALUES ('Ryan', 'Viglione', 'Spanish 1, Spanish 2', 'Period 1 Spanish 1', 'Period 3 Spanish 2', 'Period 5 Spanish 2', 'Period 6 Spanish 1', 'Period 7 Spanish 1');

CREATE TABLE Period_1_Spanish_1(
	id SERIAL PRIMARY KEY,
	subject TEXT NOT NULL,
	teacher TEXT NOT NULL,
	student_first_name TEXT NOT NULL,
	student_last_name TEXT NOT NULL,
	student_graduation_year INT NOT NULL,
	student_grade INT NOT NULL);

INSERT INTO period_1_spanish_1(subject, teacher, student_first_name, student_last_name, student_graduation_year, student_grade)
VALUES ('Spanish 1', 'Viglione', 'Ally', 'Sequel', 2025, 88),
       ('Spanish 1', 'Viglione', 'Annie', 'Jenkins', 2025, 80),
	   ('Spanish 1', 'Viglione', 'Mario', 'Worcester', 2024, 77);

CREATE TABLE Period_3_Spanish_2(
	id SERIAL PRIMARY KEY,
	subject TEXT NOT NULL,
	teacher TEXT NOT NULL,
	student_first_name TEXT NOT NULL,
	student_last_name TEXT NOT NULL,
	student_graduation_year INT NOT NULL,
	student_grade INT NOT NULL);

CREATE TABLE Period_5_Spanish_2(
	id SERIAL PRIMARY KEY,
	subject TEXT NOT NULL,
	teacher TEXT NOT NULL,
	student_first_name TEXT NOT NULL,
	student_last_name TEXT NOT NULL,
	student_graduation_year INT NOT NULL,
	student_grade INT NOT NULL);

CREATE TABLE Period_6_Spanish_1(
	id SERIAL PRIMARY KEY,
	subject TEXT NOT NULL,
	teacher TEXT NOT NULL,
	student_first_name TEXT NOT NULL,
	student_last_name TEXT NOT NULL,
	student_graduation_year INT NOT NULL,
	student_grade INT NOT NULL);

CREATE TABLE Period_7_Spanish_1(
	id SERIAL PRIMARY KEY,
	subject TEXT NOT NULL,
	teacher TEXT NOT NULL,
	student_first_name TEXT NOT NULL,
	student_last_name TEXT NOT NULL,
	student_graduation_year INT NOT NULL,
	student_grade INT NOT NULL);

INSERT INTO period_3_spanish_2(subject, teacher, student_first_name, student_last_name, student_graduation_year, student_grade)
VALUES ('Spanish 2', 'Viglione', 'Tom', 'Numan', 2023, 60),
       ('Spanish 2', 'Viglione', 'John', 'Jenkins', 2023, 90),
	   ('Spanish 2', 'Viglione', 'Maria', 'Arthur', 2024, 77);

INSERT INTO period_5_spanish_2(subject, teacher, student_first_name, student_last_name, student_graduation_year, student_grade)
VALUES ('Spanish 2', 'Viglione', 'Hector', 'Perron', 2024, 70),
       ('Spanish 2', 'Viglione', 'Kyle', 'Joseph', 2024, 50),
	   ('Spanish 2', 'Viglione', 'Neimar', 'Zanzibar', 2024, 97);

INSERT INTO period_6_spanish_1(subject, teacher, student_first_name, student_last_name, student_graduation_year, student_grade)
VALUES ('Spanish 1', 'Viglione', 'Luis', 'Smith', 2024, 80),
       ('Spanish 1', 'Viglione', 'Ashley', 'Kirkman', 2024, 90),
	   ('Spanish 1', 'Viglione', 'Pablo', 'Mendez', 2024, 57);

INSERT INTO period_7_spanish_1(subject, teacher, student_first_name, student_last_name, student_graduation_year, student_grade)
VALUES ('Spanish 1', 'Viglione', 'Mohammed', 'Kabsa', 2024, 92),
       ('Spanish 1', 'Viglione', 'Tyrone', 'Freidman', 2024, 88),
	   ('Spanish 1', 'Viglione', 'Georgia', 'Athnes', 2024, 66);
