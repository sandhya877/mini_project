from flask import Flask, render_template, request
from flask import url_for

import sqlite3
  
app = Flask(__name__)
  
  
@app.route('/')
@app.route('/home')
def index():
    return render_template("stations.html")
  
connect = sqlite3.connect('database1.db')
connect.execute(
    'CREATE TABLE IF NOT EXISTS PARTICIPANTS (name TEXT, \
    email TEXT, city TEXT, country TEXT, phone TEXT)')
connect.execute(
    'CREATE TABLE IF NOT EXISTS VACANCY1 (source TEXT, \
    destination TEXT, coach TEXT, berth TEXT)')

##participants chart

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        city = request.form['city']
        country = request.form['country']
        phone = request.form['phone']
  
        with sqlite3.connect("database1.db") as users:
            cursor = users.cursor()
            cursor.execute("INSERT INTO PARTICIPANTS \
            (name,email,city,country,phone) VALUES (?,?,?,?,?)",
                           (name, email, city, country, phone))
            users.commit()
        return render_template("index.html")
    else:
        return render_template('join.html')  
    
##vacancy chart

@app.route('/vacancy', methods=['GET', 'POST'])
def vacancy():
    if request.method == 'POST':
        source = request.form['source']
        destination = request.form['destination']
        coach = request.form['coach']
        berth = request.form['berth']
  
        with sqlite3.connect("database1.db") as users:
            cursor = users.cursor()
            cursor.execute("INSERT INTO VACANCY1 \
            (source,destination,coach,berth) VALUES (?,?,?,?)",
                           (source, destination, coach, berth))
            users.commit()
        return render_template("vacancy_index.html")
    else:
        return render_template('vacancy.html')  
    
@app.route('/vacancylist')
def vacancylist():
    connect = sqlite3.connect('database1.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM VACANCY1')
  
    data = cursor.fetchall()
    return render_template("vacancylist.html", data=data)

@app.route('/vacancylist1')
def vacancylist1():
    connect = sqlite3.connect('database1.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM VACANCY1')
  
    data = cursor.fetchall()
    return render_template("vacancylist1.html", data=data)



@app.route('/participants')
def participants():
    connect = sqlite3.connect('database1.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM PARTICIPANTS')
  
    data = cursor.fetchall()
    return render_template("participants.html", data=data)


if __name__ == '__main__':
    app.run(debug=False)