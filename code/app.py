from flask import Flask, render_template, request
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/snippets')
def snippets():
    con = sqlite3.connect('snippets.db')
    c = con.cursor()
    c.execute('SELECT * FROM snippets')
    rows = c.fetchall()
    con.close()
    return render_template('snippets.html', rows=rows)