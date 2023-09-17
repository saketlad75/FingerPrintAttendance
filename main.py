from flask import Flask,render_template,request
import mysql.connector
conn = mysql.connector.connect(host="127.0.0.1",
                               user="root",
                               password="@Svlad2305",
                               database="dept",
                               auth_plugin='mysql_native_password')
cursor = conn.cursor()
app = Flask(__name__)

@app.route('/register',methods=['POST'])
def register():
    name = request.form.get('name')
    faculty_ID = request.form.get('faculty_id')
    email = request.form.get('email')
    password = request.form.get('password')
    branch = request.form.get('branch')

    query = "INSERT INTO faculty (name,faculty_ID,email,password,branch) VALUES(%s, %s, %s, %s, %s)"
    cursor.execute(query,(name, faculty_ID, email, password, branch))
    conn.commit()
    return "User registered Successfully"
@app.route('/login_validation',methods=['POST'])
#Whenever we use form us use POST Method,the data is stored in the requests
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')
    query = "SELECT * FROM `faculty` WHERE `email` LIKE %s and `password` LIKE %s"
    cursor.execute(query,(email,password))
    users = cursor.fetchall()
    #return "The email is {} and the password is {}".format(email,password )
    if len(users)>0:
        return render_template('dash.html')
    else:
        return render_template('home.html')
    #print(users)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/register',methods=['POST','GET'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        faculty_ID = request.form.get('faculty_id')
        email = request.form.get('email')
        password = request.form.get('password')
        branch = request.form.get('branch')

        # Insert the user data into the 'faculty' table
        query = "INSERT INTO faculty (name, faculty_ID, email, password, branch) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (name, faculty_ID, email, password, branch))
        conn.commit()
        return "User registered successfully"
    else:
        return render_template('register.html')
    #return render_template('register.html')
if __name__ == '__main__':
    app.run(debug=True)