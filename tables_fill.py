from tables_preparation import cursor, conn

persons_data = [
    ('John', 'red', 1000),
    ('Anna', 'red', 2000),
    ('James', 'green', 500),
    ('Karl', 'black', 2500)
]


cars_data = [
    ('BMW M1', 'blue', 700),
    ('BMW M2', 'black', 1700),
    ('BMW M3', 'black', 2300),
    ('Fiat M1', 'red', 1500),
    ('Fiat M2', 'red', 1000),
    ('Chevrolet M1', 'green', 501)
]


cursor.executemany('INSERT INTO Persons (name, favorite_color, profit) VALUES (?, ?, ?)', persons_data)


cursor.executemany('INSERT INTO Cars (model, color, price) VALUES (?, ?, ?)', cars_data)


conn.commit()


conn.close()
