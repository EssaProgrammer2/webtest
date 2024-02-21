from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
import sqlite3
import json

#essa

app = Flask(__name__)
CORS(app)
api = Api(app)
conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS dataorang (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

class adddata(Resource):
  def post(self, name, password):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM dataorang")
    datas = cur.fetchall()
    usernames = []
    passwords = []
    u = 0
    while u<len(datas):
      user_data = list(datas[u])
      usernames.append(user_data[1])
      passwords.append(user_data[2])
      u = u + 1
    conn.commit()
    if name not in usernames and password not in passwords:
      conn = sqlite3.connect("database.db")
      cur = conn.cursor()
      cur.execute("INSERT INTO dataorang (name, password) VALUES (?, ?)", (name, password))
      conn.commit()


class getdata(Resource):
  def get(self):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM dataorang")
    haghag = cur.fetchall()
    conn.commit()
    return haghag

api.add_resource(adddata, "/post/data/name=<name>&password=<password>")
api.add_resource(getdata, "/get/data")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=7070, debug=True)