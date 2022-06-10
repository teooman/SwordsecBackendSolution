from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os, json
import requests
from rq import Queue
from rq.job import Job
import redis
from mypackage import fetcher

conn = psycopg2.connect(
        host="postgres",
        database="swordsec_test",
        user="swordsecuser",
        password="password")

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS users;')

cur.execute("""CREATE TABLE users (id serial PRIMARY KEY, first_name varchar (150),
                                 last_name varchar (150),
                                 email varchar (50),
                                 gender varchar (50),
                                 ip_address varchar (20),
                                 user_name varchar (50),
                                 user_agent text,
                                 country text);""")
cur.close()
conn.commit()
app = Flask(__name__)

r = redis.Redis(host='redis', port=6379)
q = Queue(connection=r)



@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    for i in range(1,11):
        task = q.enqueue(fetcher.maker,i)

    return f"Task has been sent! {task.id}"

if __name__ == "__main__":
    port = 5000
    app.run(debug=True, host='0.0.0.0', port=port)
