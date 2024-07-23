import sqlite3

conn = sqlite3.connect('data1.db')
cursor = conn.cursor()

try:
    query = '''
        SELECT Persons.name, Cars.model, Cars.color, Cars.price, Persons.profit
        FROM Persons
        JOIN (
            SELECT Persons.name, Persons.favorite_color, MIN(Cars.model) AS model
            FROM Persons
            LEFT JOIN Cars ON Persons.favorite_color = Cars.color AND Cars.price <= Persons.profit
            GROUP BY Persons.name, Persons.favorite_color
        ) cheapest_cars ON Persons.name = cheapest_cars.name AND Persons.favorite_color = cheapest_cars.favorite_color
        LEFT JOIN Cars ON cheapest_cars.model = Cars.model
        WHERE Cars.price <= Persons.profit
        ORDER BY Persons.name ASC
    '''

    cursor.execute(query)

    print("name  model    color  price   profit")
    print("----  -------  -----  ------  ------")
    for row in cursor.fetchall():
        person_name, model, color, price, profit = row
        print(f"{person_name}  {model}  {color}  {price}  {profit}")

except sqlite3.Error as e:
    print(f"Error: {e}")

finally:
    # Close the connection
    conn.close()
