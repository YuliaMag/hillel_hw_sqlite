import sqlite3

conn = sqlite3.connect('data1.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Persons (
        name TEXT,
        favorite_color TEXT,
        profit REAL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cars (
        model TEXT,
        color TEXT,
        price REAL
    )
''')


conn.commit()
