from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app= Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Vamsi@1984'
app.config['MYSQL_DB'] = 'medicination'


mysql = MySQL(app)

@app.route('/')
def home_page():
    return render_template('index.html')
  
@app.route('/about')
def about_page():
    return render_template('about.html')   

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/check')
def check_page():
    title= "Thank you ! "
    return render_template('check.html',title=title)

@app.route('/send', methods =['GET','POST' ]  )
def send( ):
    if request.method=='POST':
        name = request.form['name']
        address = request.form['address']
        email = request.form['email']
        phone = request.form['phone']  
        message = request.form['message']
        cur=mysql.connection.cursor()
        cur.execute(" INSERT INTO vamsi(name, address, email, phone, message)  VALUES( %s, %s, %s, %s, %s )", (name, address, email, phone, message) )
        mysql.connection.commit()
        cur.close()
        return 'success'
           
        
    return render_template('contact.html')
  

if __name__=="__main__":
    app.run(debug=True,port=8000)