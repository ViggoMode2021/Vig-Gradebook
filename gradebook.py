from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

#TO DO:

#Make photos
#Duplicate html, update, and query pages
#CSS
#Add teachers
#Add administrators
#Add back to home button
#Add delete option
#Table length?
#Add advanced queries
#Add update integer

hostname = 'localhost'
database = 'Gradebook'
username = 'postgres'
pwd = ''
port_id = 5432
conn = None
cur = None

@app.route('/')
def main():
    title_two = 'Gradebook main page'
    return render_template('main_page.html', title=title_two)

@app.route('/main_page_2')
def main_page_2():
    title_two = 'Gradebook main page'
    return render_template('main_page_2.html', title=title_two)

@app.route('/period_1_Spanish_1_enroll')
def period_1_Spanish_1_enroll():
    title_two = 'enroll or check enrollment'
    return render_template('period_1_Spanish_1_enroll.html', title=title_two)

@app.route('/period_3_Spanish_2_enroll')
def period_3_Spanish_2_enroll():
    title_two = 'enroll or check enrollment'
    return render_template('period_3_Spanish_2_enroll.html', title=title_two)

@app.route('/period_5_Spanish_2_enroll')
def period_5_Spanish_2_enroll():
    title_two = 'enroll or check enrollment'
    return render_template('period_5_Spanish_2_enroll.html', title=title_two)

@app.route('/regular_verbs_worksheet_period_1')
def regular_verbs_worksheet_period_1():
    title_two = 'regular_verbs_worksheet_period_1'
    return render_template('regular_verbs_worksheet_period_1.html', title=title_two)


@app.route('/update', methods=['POST'])
def update():
    try:
        conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)

        cur = conn.cursor()

        insert_script = "INSERT INTO period_1_spanish_1 (subject, teacher, student_first_name, student_last_name, student_graduation_year, student_grade) VALUES (%s, %s, %s, %s, %s, %s)"

        subject = request.form.get("subject")
        teacher = request.form.get("teacher")
        first_name = request.form.get("first name")
        last_name = request.form.get("last name")
        graduation_year = request.form.get("graduation year")
        grade = request.form.get("grade")

        title_two = "Period 1 Spanish 1 enroll or check enrollment" #This title appears once the enroll button is hit.

        insert_values = [(subject, teacher, first_name, last_name, graduation_year, grade)]

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

    return render_template('period_1_Spanish_1_enroll.html',title =title_two)

@app.route('/query', methods=['POST'])
def query():
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)

    c = conn.cursor()

    s = "SELECT * FROM period_1_spanish_1"
    c.execute(s)
    records_2 = c.fetchall()
    #print(records)

    #loop through results
    #print_records = ''
    #for record_2 in records_2[0:6]:
        #print_records += str(record_2) + "\n"

    conn.commit()
    conn.close()

    return render_template('query_page.html', records_2 = records_2)

@app.route('/query_regular_verbs_ws_p1', methods=['POST'])
def query_regular_verbs_ws_p1():
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)

    c = conn.cursor()

    s = "SELECT * FROM period_1_spanish_1"
    c.execute(s)
    records_2 = c.fetchall()
    #print(records)

    #loop through results
    #print_records = ''
    #for record_2 in records_2[0:6]:
        #print_records += str(record_2) + "\n"

    #conn.commit()

    #conn.close()

    return render_template('regular_verbs_worksheet_period_1.html', records_2 = records_2)

@app.route('/update_2', methods=['POST'])
def update_2():
    try:
        conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)

        cur = conn.cursor()

        insert_script_2 = "INSERT INTO period_3_spanish_2 (subject, teacher, student_first_name, student_last_name, student_graduation_year, student_grade) VALUES (%s, %s, %s, %s, %s, %s)"

        subject_2 = request.form.get("subject_2")
        teacher_2 = request.form.get("teacher_2")
        first_name_2 = request.form.get("first name_2")
        last_name_2 = request.form.get("last name_2")
        graduation_year_2 = request.form.get("graduation year_2")
        grade_2 = request.form.get("grade_2")

        title_two = "Period 3 Spanish 2 enroll or check enrollment" #This title appears once the enroll button is hit.

        insert_values_2 = [(subject_2, teacher_2, first_name_2, last_name_2, graduation_year_2, grade_2)]

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

    return render_template('period_3_Spanish_2_enroll.html', title = title_two)

@app.route('/query_2', methods=['POST'])
def query_2():
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)

    c = conn.cursor()

    s_2 = "SELECT * FROM period_3_spanish_2"
    c.execute(s_2)
    records_3 = c.fetchall()

    return render_template('query_page_period_3.html', records_3 = records_3)

@app.route('/update_3', methods=['POST'])
def update_3():
    try:
        conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)

        cur = conn.cursor()

        insert_script_3 = "INSERT INTO period_5_spanish_2 (subject, teacher, student_first_name, student_last_name, student_graduation_year, student_grade) VALUES (%s, %s, %s, %s, %s, %s)"

        subject_3 = request.form.get("subject_3")
        teacher_3 = request.form.get("teacher_3")
        first_name_3 = request.form.get("first name_3")
        last_name_3 = request.form.get("last name_3")
        graduation_year_3 = request.form.get("graduation year_3")
        grade_3 = request.form.get("grade_3")

        title_two = "Period 5 Spanish 2 enroll or check enrollment" #This title appears once the enroll button is hit.

        insert_values_3 = [(subject_3, teacher_3, first_name_3, last_name_3, graduation_year_3, grade_3)]

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

    return render_template('period_5_Spanish_2_enroll.html', title = title_two)

@app.route('/query_3', methods=['POST'])
def query_3():
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)

    c = conn.cursor()

    s_3 = "SELECT * FROM period_5_spanish_2"
    c.execute(s_3)
    records_4 = c.fetchall()

    conn.close()

    return render_template('query_page_period_5.html', records_4 = records_4)

@app.route('/update_period_3_grades', methods=['POST'])
def update_period_3_grades():
    return render_template('update_period_3_grades.html')

@app.route('/update_period_3_grades_button', methods=['POST'])
def update_period_3_grades_button():
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)

    cur = conn.cursor()

    last_name_3 = request.form.get("student_last_name")
    new_grade_3 = request.form.get("student_new_grade")

    period_3_update_grades_query = "UPDATE period_3_spanish_2 SET student_grade = (%s) WHERE student_last_name = (%s)"

    insert_values = [(new_grade_3, last_name_3)]

    for record in insert_values:
        cur.execute(period_3_update_grades_query, record)

    conn.commit()

    return render_template('update_period_3_grades.html')

if __name__ == "__main__":
    app.run(debug=True)
