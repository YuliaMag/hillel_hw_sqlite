import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('data1.db')
cursor = conn.cursor()

try:
    query = '''
 WITH AffordableCar AS (
    SELECT Persons.name AS person_name, Cars.model AS car_model, Cars.price AS car_price
    FROM Persons
    JOIN Cars ON Persons.favorite_color = Cars.color
    WHERE Persons.profit >= Cars.price
),
CheapestCar AS (
    SELECT person_name, MIN(car_price) AS min_price
    FROM AffordableCar
    GROUP BY person_name
)
SELECT Persons.name AS person_name,
    COALESCE(AffordableCar.car_model, 'NULL') AS car_model,
    Persons.favorite_color,
    COALESCE(AffordableCar.car_price, 'NULL') AS car_price,
	Persons.profit
FROM Persons
LEFT JOIN 
    CheapestCar ON Persons.name = CheapestCar.person_name
LEFT JOIN AffordableCar ON CheapestCar.person_name = AffordableCar.person_name AND CheapestCar.min_price = AffordableCar.car_price
ORDER BY Persons.name;
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
