# gradebook

Title: Ryan's Gradebook

Description: 

This application 'Ryan's Gradebook' serves as a basic CRUD gradebook for three fictional Spanish classes.
It was created with Flask and is backed up by a Postgresql database through
psycopg2. This project makes use of HTML and CSS through the Jinja template,
alongside some Bootstrap and custom HTML and CSS. Essentially, Ryan's Gradebook
is an example of a fullstack application that showcases core frontend and backend principles.

In order for one to use this application, one must create a database titled 'Gradebook'
on a Postgres server. After, they should run the 'dump' file 'gradebook.sql', which will
create the tables (for the fictional Spanish classes) and populate them with some examples of fictional students. Each table has 
7 columns that ar NOT NULL (asking for information like student names and grades). There is another 
table titled 'assignments' that showcases a 1-1 relationship with a foreign key to the Period 1 Spanish 1
table. I have not figured out the best and most efficient way to implement other foreign key
relations, but I hope to expand on this with further research and development of this app. Lastly, in the app.py file,
the user should configure the database settings for their own database in order for psycopg2 to connect.

Now, here is where the explanation of the front and back end working together will
be laid out. When the user loads the app, the app will open to the main page and allow the user
to click to whichever class they want with the navbar at the top of the screen or photos below.
Said link will bring them to the respective class' enroll page, where they will be either the option
to fill out 7 fields in a html form, or just check the class roster. If they decide to 
check the class roster without enrolling a new student, they will click the 'show class roster'
button, which will direct them to a new page that shows a html table replicate of what is 
in the Postgres database. This table is population with the results pulled from 
the database through a 'SELECT *' statement run through psycopg2. This is an area where the app
demonstrates a 'GET' request. This table also has a red button to 'unenroll student', which will
call a 'DELETE' request through psycopg2 and remove the student from the Postgres backend
and also update the frontend HTML page so that the student disappears. The user can also update the
student grade by filling out the respective input box 'update grade here' with a new grade and clicking
the update grade button. This will run an 'UPDATE' query to update the respective student's grade on 
both the backend (Postgres) and frontend (HTML). This functionality demonstrates a 'PUT/PATCH' request.

Back on the Spanish class' enroll page, the user can fill out the 7 fields of the request boxes in order
to enroll a new student to the class. Once all fields are filled out, the user clicks the 'enroll student'
button and the new student is added to the table with a 'INSERT' statement. The new student is added to the 
Postgres database and the user can click on the 'show class roster button' to see their added student on the
frontend. This is a demonstration of a 'POST' request.

Conclusion:

The project's design evolved once I started implementing how the frontend was going to work and operate
alongside the backend. My goal is to continue working on this project and make it most robust and customizable.
I would like to add more features, such as an assignment creator, which would allow the user to create
new assignments and designate how it will factor in and affect the students' grades. I would like to add
functionality to implement more advanced and creative queries, such as filtering students by grade range,
sorting by last name, and other sorting options that can allow the user to select specific data to review.
Thank you for reading and please stay tuned for updates to this project!

-Ryan Viglione
