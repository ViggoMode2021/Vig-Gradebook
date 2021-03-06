
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

CREATE TABLE assignments_period_1_spanish_1_for_real(
    id SERIAL PRIMARY KEY,
    assignment_name TEXT NOT NULL,
    category TEXT NOT NULL,
    due_date TEXT NOT NULL,
    overall_points INT NOT NULL
    );

ALTER TABLE assignments_period_1_spanish_1_for_real
ADD CONSTRAINT student_id
FOREIGN KEY (id) REFERENCES Period_1_Spanish_1(id)

CREATE TABLE assignments_period_1_spanish_1_results(
    id SERIAL PRIMARY KEY,
    score INT NOT NULL,
    student_id INT NOT NULL,
    assignment_id INT NOT NULL,
    FOREIGN KEY ("student_id") REFERENCES Period_1_Spanish_1("id") ON DELETE CASCADE,
    FOREIGN KEY ("assignment_id") REFERENCES assignments_period_1_spanish_1_for_real("id") ON DELETE CASCADE);

SELECT
    s.student_last_name,
    asi.score,
    an.assignment_name
FROM period_1_spanish_1 s
INNER JOIN assignments_period_1_spanish_1_results AS asi
ON as.student_id = s.id
INNER JOIN assignments_period_1_spanish_1_for_real an
ON an.id = asi.assignment_id
ORDER BY an.assignment_name asc;

CREATE TABLE period_1_spanish_1_attendance(
id SERIAL PRIMARY KEY,
attendance_date VARCHAR NOT NULL,
attendance_status TEXT NOT NULL,
student_id INT NOT NULL,
FOREIGN KEY ("student_id") REFERENCES Period_1_Spanish_1("id") ON DELETE CASCADE);

SELECT
month, number_day, attendance_status
FROM period_1_spanish_1_attendance
WHERE month = 'September' AND number_day = 2;

SELECT
student_first_name,
student_last_name,
attendance_date,
number_day,
attendance_status
FROM period_1_spanish_1_attendance att
JOIN period_1_spanish_1 s
ON att.student_id = s.id
WHERE att.id = {0}
ORDER BY s.student_last_name ASC;
