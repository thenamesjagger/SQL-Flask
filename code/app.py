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

@app.route('/snippet/<int:id>', methods=['DELETE'])
def delete_snippet(id):
    con = sqlite3.connect('snippets.db')
    c = con.cursor()
    c.execute(f'DELETE FROM snippets WHERE id={id}')
    con.commit()
    con.close()
    return '', 200

@app.route('/snippets/add', methods=['GET', 'POST'])
def add_snippet():
    if request.method == 'POST':
        # Get the user's input
        snippet = request.form['snippet']
        description = request.form['description']

        # Connect to the database and add the new snippet and description
        con = sqlite3.connect('snippets.db')
        c = con.cursor()
        c.execute('INSERT INTO snippets (description, snippet) VALUES (?,?)', (description, snippet))
        con.commit()
        con.close()

        # Redirect the user back to the main snippets page
        return render_template('snippets.html')

    return render_template('addsnippets.html')
