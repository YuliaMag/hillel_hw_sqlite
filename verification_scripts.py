import sqlite3


conn = sqlite3.connect('data1.db')
cursor = conn.cursor()


cursor.execute('SELECT * FROM Persons')
print("\nPersons:")
for row in cursor.fetchall():
    print(row)


cursor.execute('SELECT * FROM Cars')
print("\nCars:")
for row in cursor.fetchall():
    print(row)


conn.close()
