from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

@app.route('/')
def main():
    title_two = 'Gradebook main page'
    return render_template('main_page.html', title=title_two)


hostname = 'localhost'
database = 'Gradebook'
username = 'postgres'
pwd = ''
port_id = 5432
conn = None
cur = None

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
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        graduation_year = request.form.get("graduation year")
        grade = request.form.get("grade")

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

    return render_template('main_page.html')

if __name__ == "__main__":
    app.run(debug=True)
