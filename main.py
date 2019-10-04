from bottle import route, run, template, static_file, request
import sqlite3


@route("/")
def home():
    return static_file("home.html", root="html")

@route('/show')
def index():
    user_id = request.query["user_id"]
    return template('<b>Hello {{name}}</b>!', name=user_id)

def get_trajectory(user_id):
    dbname = "db.sqlite"
    with sqlite3.connect(dbname) as con:
        cur = con.cursor()
        con.commit()

    

run(host='localhost', port=8080)
