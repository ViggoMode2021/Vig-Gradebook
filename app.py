from flask import Flask, render_template, request, redirect, url_for
import psycopg2
app = Flask(__name__)

#Below is the database information
hostname = 'localhost'
database = 'Gradebook'
username = 'postgres'
pwd = '' #This won't be shared. Teachers and students of NuCamp that wish
# to replicate this database should view README.md for more information. Thank you.
port_id = 5432
conn = None
cur = None

@app.route('/') #ROUTING FOR MAIN PAGE
def main():
    title_two = 'Gradebook main page'
    return render_template('main_page.html', title=title_two)

@app.route('/period_1_Spanish_1_enroll') #ROUTING FOR PERIOD 1 SPANISH 1 ENROLL STUDENT PAGE
def period_1_Spanish_1_enroll():
    return render_template('period_1_Spanish_1_enroll.html')

@app.route('/period_3_Spanish_2_enroll') #ROUTING FOR PERIOD 3 SPANISH 2 ENROLL STUDENT PAGE
def period_3_Spanish_2_enroll():
    return render_template('period_3_Spanish_2_enroll.html')

@app.route('/period_5_Spanish_2_enroll') #ROUTING FOR PERIOD 2 SPANISH 2 ENROLL STUDENT PAGE
def period_5_Spanish_2_enroll():
    return render_template('period_5_Spanish_2_enroll.html')

@app.route('/regular_verbs_worksheet_period_1')
def regular_verbs_worksheet_period_1():
    return render_template('regular_verbs_worksheet_period_1.html')

#period_1_spanish_1 enroll student #CREATE
@app.route('/update', methods=['POST'])
def update():
    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)

        cur = conn.cursor()

        insert_script = "INSERT INTO period_1_spanish_1 (subject, teacher, student_first_name, student_last_name, student_graduation_year, student_grade) VALUES (%s, %s, %s, %s, %s, %s)"

        subject = request.form.get("subject")
        teacher = request.form.get("teacher")
        first_name = request.form.get("first name")
        last_name = request.form.get("last name")
        graduation_year = request.form.get("graduation year")
        grade = request.form.get("grade")

        insert_values = [(subject, teacher, first_name,
                          last_name, graduation_year, grade)]

        for record in insert_values:
            cur.execute(insert_script, record)

        cur.execute('SELECT * FROM period_1_spanish_1')
        for record in cur.fetchall():
            print(record)

        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return render_template('period_1_Spanish_1_enroll.html')

#period_1_spanish_1 show class roster #READ
@app.route('/query', methods=['GET'])
def query():
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    c = conn.cursor()

    s = "SELECT * FROM period_1_spanish_1"
    c.execute(s)
    records_2 = c.fetchall()

    conn.commit()
    conn.close()

    return render_template('query_page.html', records_2=records_2)

#period_1_sort_last_name_alphabetically
@app.route('/alphabetically_p1', methods=['GET'])
def alphabetically_p1():
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    c = conn.cursor()

    s = "SELECT * FROM period_1_spanish_1 ORDER BY student_last_name ASC"
    c.execute(s)
    records_2 = c.fetchall()

    conn.commit()
    conn.close()

    return render_template('query_page.html', records_2=records_2)

#period_1_sort_first_name_alphabetically
@app.route('/alphabetically_first_p1', methods=['GET'])
def alphabetically_first_p1():
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    c = conn.cursor()

    s = "SELECT * FROM period_1_spanish_1 ORDER BY student_first_name ASC"
    c.execute(s)
    records_2 = c.fetchall()

    conn.commit()
    conn.close()

    return render_template('query_page.html', records_2=records_2)

#period_1_sort_grade_ascending
@app.route('/grade_ASC_p1', methods=['GET'])
def grade_ASC_p1():
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    c = conn.cursor()

    s = "SELECT * FROM period_1_spanish_1 ORDER BY student_grade ASC"
    c.execute(s)
    records_2 = c.fetchall()

    conn.commit()
    conn.close()

    return render_template('query_page.html', records_2=records_2)

#period_1_sort_grade_descending
@app.route('/grade_DESC_p1', methods=['GET'])
def grade_DESC_p1():
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    c = conn.cursor()

    s = "SELECT * FROM period_1_spanish_1 ORDER BY student_grade DESC"
    c.execute(s)
    records_2 = c.fetchall()

    conn.commit()
    conn.close()

    return render_template('query_page.html', records_2=records_2)

#period_1_spanish_1_delete_student #DELETE
@app.route('/delete/<string:id>', methods = ['DELETE', 'GET'])
def delete_student(id):
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    cur = conn.cursor()

    cur.execute('DELETE FROM period_1_spanish_1 WHERE id = {0}'.format(id))
    conn.commit()
    s = "SELECT * FROM period_1_spanish_1"
    cur.execute(s)
    conn.close()
    return redirect(url_for('query'))

#period_1_spanish_1_update_grade #UPDATE
@app.route('/period_1_update_grade/<id>', methods = ['PATCH', 'GET', 'POST'])
def period_1_update_grade(id):
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    updated_grade = request.form.get("update grade")

    cur = conn.cursor()

    cur.execute("""UPDATE period_1_spanish_1 
    SET student_grade = %s 
    WHERE id = %s""", (updated_grade, id))

    conn.commit()

    s = "SELECT * FROM period_1_spanish_1"
    cur.execute(s)
    conn.close()
    return redirect(url_for('query'))

#period_1_spanish_edit_assignment_grades
@app.route('/assignment', methods=['GET', 'POST'])
def assignment():
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    c = conn.cursor()

    s = "SELECT * FROM assignments_period_1_spanish_1"
    c.execute(s)
    assignment_1 = c.fetchall()

    conn.commit()
    conn.close()

    return render_template('assignment.html', assignment_1 = assignment_1)

#period_1_spanish_1_new_assignment_creation
@app.route('/new_assignment', methods=['POST'])
def new_assignment():
    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)

        cur = conn.cursor()

        insert_script = "INSERT INTO assignments_period_1_spanish_1_for_real(assignment_name, category, due_date, overall_points) VALUES (%s, %s, %s, %s)"

        assignment_name = request.form.get("assignment name")
        category = request.form.get("category")
        due_date = request.form.get("due date")
        overall_points = request.form.get("max points")

        insert_values = [(assignment_name, category, due_date,
                          overall_points)]

        for record in insert_values:
            cur.execute(insert_script, record)

        a_2 = """ALTER TABLE period_1_spanish_1 ADD COLUMN IF NOT EXISTS assignment_id INT"""

        cur.execute(a_2)
        cur.execute("""ALTER TABLE period_1_spanish_1 ADD COLUMN IF NOT EXISTS assignment_name TEXT""")
        cur.execute("""ALTER TABLE period_1_spanish_1 ADD COLUMN IF NOT EXISTS assignment_1_grade INT""")
        assignment_id = request.form.get("assignment id")
        assignment_name = request.form.get("assignment name")
        cur.execute("INSERT INTO period_1_spanish_1(assignment_id, assignment_name) VALUES (%s, %s)", (assignment_id, assignment_name))

        conn.commit()

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return render_template('assignment.html')

#period_1_spanish_1
@app.route('/new_assignment_update', methods=['GET'])
def new_assignment_update():
    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)

        cur = conn.cursor()

        s = 'SELECT * FROM assignments_period_1_spanish_1_for_real'
        cur.execute(s)
        assignment_titles = cur.fetchall()

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return render_template('assignment.html', assignment_titles = assignment_titles)

#period_1_spanish_1_edit_assignment_grade_page_route
@app.route('/edit_assignment_grade/<string:id>', methods=['GET'])
def edit_assignment_grade(id):
    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)

        cur = conn.cursor()

        s = 'SELECT * FROM assignments_period_1_spanish_1_for_real WHERE id = {0}'.format(id)
        cur.execute(s)
        assignment_titles = cur.fetchall()

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return render_template('edit_assignment_grade.html', assignment_titles = assignment_titles)

@app.route('/period_1_update_assignment_grade/<string:id>', methods=['POST'])
def period_1_update_assignment_grade(id):
    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)

        cur = conn.cursor()

        s = 'SELECT * FROM assignments_period_1_spanish_1_for_real WHERE id = {0}'.format(id)
        cur.execute(s)
        assignment_titles = cur.fetchall()

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return render_template('edit_assignment_grade.html', assignment_titles = assignment_titles)

#period_3_spanish_2 enroll student #CREATE
@app.route('/update_2', methods=['POST'])
def update_2():
    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)

        cur = conn.cursor()

        insert_script_2 = "INSERT INTO period_3_spanish_2 (subject, teacher, student_first_name, student_last_name, student_graduation_year, student_grade) VALUES (%s, %s, %s, %s, %s, %s)"

        subject_2 = request.form.get("subject_2")
        teacher_2 = request.form.get("teacher_2")
        first_name_2 = request.form.get("first name_2")
        last_name_2 = request.form.get("last name_2")
        graduation_year_2 = request.form.get("graduation year_2")
        grade_2 = request.form.get("grade_2")

        insert_values_2 = [(subject_2, teacher_2, first_name_2,
                            last_name_2, graduation_year_2, grade_2)]

        for record in insert_values_2:
            cur.execute(insert_script_2, record)

        cur.execute('SELECT * FROM period_3_spanish_2')
        for record in cur.fetchall():
            print(record)

        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return render_template('period_3_Spanish_2_enroll.html')

#period_3_spanish_2 enroll student #READ
@app.route('/query_2', methods=['GET'])
def query_2():
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    c = conn.cursor()

    s_2 = "SELECT * FROM period_3_spanish_2"
    c.execute(s_2)
    records_3 = c.fetchall()

    conn.close()

    return render_template('query_page_period_3.html', records_3=records_3)

#period_3_sort_last_name_alphabetically
@app.route('/alphabetically_p3', methods=['GET'])
def alphabetically_p3():
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    c = conn.cursor()

    s = "SELECT * FROM period_3_spanish_2 ORDER BY student_last_name ASC"
    c.execute(s)
    records_3 = c.fetchall()

    conn.commit()
    conn.close()

    return render_template('query_page_period_3.html', records_3=records_3)

#period_3_sort_first_name_alphabetically
@app.route('/alphabetically_first_p3', methods=['GET'])
def alphabetically_first_p3():
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    c = conn.cursor()

    s = "SELECT * FROM period_3_spanish_2 ORDER BY student_first_name ASC"
    c.execute(s)
    records_3 = c.fetchall()

    conn.commit()
    conn.close()

    return render_template('query_page_period_3.html', records_3=records_3)

#period_1_sort_grade_ascending
@app.route('/grade_ASC_p3', methods=['GET'])
def grade_ASC_p3():
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    c = conn.cursor()

    s = "SELECT * FROM period_3_spanish_2 ORDER BY student_grade ASC"
    c.execute(s)
    records_3 = c.fetchall()

    conn.commit()
    conn.close()

    return render_template('query_page_period_3.html', records_3=records_3)

#period_3_sort_grade_descending
@app.route('/grade_DESC_p3', methods=['GET'])
def grade_DESC_p3():
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    c = conn.cursor()

    s = "SELECT * FROM period_3_spanish_2 ORDER BY student_grade DESC"
    c.execute(s)
    records_3 = c.fetchall()

    conn.commit()
    conn.close()

    return render_template('query_page_period_3.html', records_3=records_3)

#period_3_spanish_2_delete_function
@app.route('/delete_student_2/<string:id>', methods = ['DELETE','GET'])
def delete_student_2(id):
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    cur = conn.cursor()

    cur.execute('DELETE FROM period_3_spanish_2 WHERE id = {0}'.format(id))
    conn.commit()
    s = "SELECT * FROM period_1_spanish_1"
    cur.execute(s)
    conn.close()
    return redirect(url_for('query_2'))

#period_3_spanish_2_update_grade #UPDATE
@app.route('/period_3_update_grade/<id>', methods = ['PATCH', 'GET', 'POST'])
def period_3_update_grade(id):
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    updated_grade_2 = request.form.get("update grade 2")

    cur = conn.cursor()

    cur.execute("""UPDATE period_3_spanish_2 
    SET student_grade = %s 
    WHERE id = %s""", (updated_grade_2, id))

    conn.commit()

    s = "SELECT * FROM period_1_spanish_1"
    cur.execute(s)

    conn.close()

    return redirect(url_for('main'))

#period_5_spanish_2 show class roster #UPDATE
@app.route('/update_3', methods=['POST'])
def update_3():
    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)

        cur = conn.cursor()

        insert_script_3 = "INSERT INTO period_5_spanish_2 (subject, teacher, student_first_name, student_last_name, student_graduation_year, student_grade) VALUES (%s, %s, %s, %s, %s, %s)"

        subject_3 = request.form.get("subject_3")
        teacher_3 = request.form.get("teacher_3")
        first_name_3 = request.form.get("first name_3")
        last_name_3 = request.form.get("last name_3")
        graduation_year_3 = request.form.get("graduation year_3")
        grade_3 = request.form.get("grade_3")

        insert_values_3 = [(subject_3, teacher_3, first_name_3,
                            last_name_3, graduation_year_3, grade_3)]

        for record in insert_values_3:
            cur.execute(insert_script_3, record)

        cur.execute('SELECT * FROM period_5_spanish_2')
        for record in cur.fetchall():
            print(record)

        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return render_template('period_5_Spanish_2_enroll.html')

#period 5 spanish 2 check class roster #READ
@app.route('/query_3', methods=['GET'])
def query_3():
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    c = conn.cursor()

    s_3 = "SELECT * FROM period_5_spanish_2"
    c.execute(s_3)
    records_4 = c.fetchall()

    conn.close()

    return render_template('query_page_period_5.html', records_4=records_4)

#period_5_spanish_2_delete_function #DELETE
@app.route('/delete_student_3/<string:id>', methods = ['POST','GET'])
def delete_student_3(id):
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    cur = conn.cursor()

    cur.execute('DELETE FROM period_5_spanish_2 WHERE id = {0}'.format(id))
    conn.commit()
    s = "SELECT * FROM period_5_spanish_2"
    cur.execute(s)
    conn.close()
    return redirect(url_for('query_3'))

#period_5_spanish_2_update_grade #UPDATE
@app.route('/period_5_update_grade/<id>', methods = ['PATCH', 'GET', 'POST'])
def period_5_update_grade(id):
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    updated_grade_3 = request.form.get("update grade 3")

    cur = conn.cursor()

    cur.execute("""UPDATE period_5_spanish_2 
    SET student_grade = %s 
    WHERE id = %s""", (updated_grade_3, id))

    conn.commit()

    s = "SELECT * FROM period_1_spanish_1"
    cur.execute(s)

    conn.close()

    return redirect(url_for('query_3'))

if __name__ == "__main__":
    app.run(debug=True)
