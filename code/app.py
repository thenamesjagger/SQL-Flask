from flask import Flask, render_template, request
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/search')
def index():
    conn = sqlite3.connect('snippets.db')
    rows = conn.execute("SELECT description FROM snippets")
    return render_template('search.html', rows=rows)

@app.route('/snippet', methods=['POST'])
def search():
    search_query = request.form['search_query']
    con = sqlite3.connect('snippets.db')
    c = con.cursor()
    c.execute('SELECT * FROM snippets WHERE description LIKE ?', ('%'+search_query+'%',))
    rows = c.fetchall()
    return render_template('snippet.html', rows=rows)

@app.route('/array')
def array():
    # Prompt the user to upload an Excel file
    excel_file = request.files['excel_file']

    # Read the Excel file using pandas
    df = pd.read_excel(excel_file)

    # Get the list of sheet names
    sheet_names = df.sheet_names

    # Prompt the user to select a sheet
    sheet = request.form['sheet']

    # Select the desired sheet
    df = df[sheet]

    # Get the list of column names
    column_names = df.columns

    # Prompt the user to select the columns
    columns = request.form['columns']

    # Select the desired columns
    df = df[columns]

    # Create a list for each column
    columns_data = [list(df[column]) for column in df.columns]

    # Return an HTML page with the input fields for selecting the sheet and columns
    return render_template('array.html', sheet_names=sheet_names, column_names=column_names)