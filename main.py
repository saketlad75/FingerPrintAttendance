from flask import Flask,render_template,request
import mysql.connector
conn = mysql.connector.connect(host="127.0.0.1",user="root",password="@Svlad2305",database="user",auth_plugin='mysql_native_password')
cursor = conn.cursor()
app = Flask(__name__)

@app.route('/register',methods=['POST'])
def register():
    name = request.form.get('name')
    faculty_ID = request.form.get('faculty_id')
    email = request.form.get('email')
    password = request.form.get('password')
    branch = request.form.get('branch')

    query = 'INSERT INTO faculty VALUES(name,faculty_ID,email,password,branch)'
    cursor.execute(query)
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
@app.route('/register')
def registration():
    return render_template('register.html')
if __name__ == '__main__':
    app.run(debug=True)