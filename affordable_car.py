import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('data1.db')
cursor = conn.cursor()

try:
    query = '''
SELECT Persons.name, Cars.model, Cars.color, Cars.price, Persons.profit 

FROM Persons

JOIN 

(SELECT Persons.name, Persons.favorite_color, MIN(Cars.price) AS min_price
    FROM Persons
    JOIN Cars ON Persons.favorite_color = Cars.color
    WHERE Cars.price <= Persons.profit
    GROUP BY Persons.name, Persons.favorite_color) cheapest_cars ON Persons.name = cheapest_cars.name AND Persons.favorite_color = cheapest_cars.favorite_color
	
JOIN Cars ON Cars.color = Persons.favorite_color AND Cars.price = cheapest_cars.min_price

ORDER BY Persons.name ASC;
    '''

    cursor.execute(query)

    data = cursor.fetchall()

    headers = ["name", "model", "color", "price", "profit"]
    table = tabulate(data, headers=headers, tablefmt="double_grid")
    print(table)

except sqlite3.Error as e:
    print(f"Error: {e}")

finally:
    conn.close()
