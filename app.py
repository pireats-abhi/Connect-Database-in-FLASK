from flask import Flask, redirect, render_template, request
from flask_mysqldb import MySQL
import yaml

db = yaml.load(open('db.yaml'))

app = Flask(__name__)

app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PORT'] = db['mysql_port']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        name = request.form.get('name')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name) VALUES(%s)", [name])
        mysql.connection.commit()
        cur.close()
        return "success"
