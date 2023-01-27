import sqlite3

con = sqlite3.connect('snippets.db')
c = con.cursor()
c.execute('CREATE TABLE snippets (id INTEGER PRIMARY KEY, description TEXT, snippet TEXT)')

# Insert some code snippets
c.execute('INSERT INTO snippets VALUES (1, "one", "def add(a, b):\n    return a + b")')
c.execute('INSERT INTO snippets VALUES (2, "two", "def subtract(a, b):\n    return a - b")')
c.execute('INSERT INTO snippets VALUES (3, "three", "def multiply(a, b):\n    return a * b")')
c.execute('INSERT INTO snippets VALUES (4, "four", "def divide(a, b):\n    return a / b")')

con.commit()
con.close()
