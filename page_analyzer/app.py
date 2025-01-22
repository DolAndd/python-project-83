import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')

@app.route("/")
def hello_world():
    return render_template('home.html')
