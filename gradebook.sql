
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

INSERT INTO period_3_spanish_2(subject, teacher, student_first_name, student_last_name, student_graduation_year, student_grade)
VALUES ('Spanish 2', 'Viglione', 'Tom', 'Numan', 2023, 60),
       ('Spanish 2', 'Viglione', 'John', 'Jenkins', 2023, 90),
	   ('Spanish 2', 'Viglione', 'Maria', 'Arthur', 2024, 77);

CREATE TABLE Period_5_Spanish_2(
	id SERIAL PRIMARY KEY,
	subject TEXT NOT NULL,
	teacher TEXT NOT NULL,
	student_first_name TEXT NOT NULL,
	student_last_name TEXT NOT NULL,
	student_graduation_year INT NOT NULL,
	student_grade INT NOT NULL);

INSERT INTO period_5_spanish_2(subject, teacher, student_first_name, student_last_name, student_graduation_year, student_grade)
VALUES ('Spanish 2', 'Viglione', 'Hector', 'Perron', 2024, 70),
       ('Spanish 2', 'Viglione', 'Kyle', 'Joseph', 2024, 50),
	   ('Spanish 2', 'Viglione', 'Neimar', 'Zanzibar', 2024, 97);

CREATE TABLE assignments_period_1_spanish_1(
    id SERIAL PRIMARY KEY,
    student_id INT,
    assignment_name TEXT NOT NULL,
    assignment_grade INT NOT NULL
    );

ALTER TABLE assignments_period_1_spanish_1
ADD CONSTRAINT student_id
FOREIGN KEY (id) REFERENCES Period_1_Spanish_1(id)
