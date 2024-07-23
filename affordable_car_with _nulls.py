import sqlite3

conn = sqlite3.connect('data1.db')
cursor = conn.cursor()

try:
    query = '''
        SELECT p.name, c.model AS model, p.favorite_color AS color, c.price AS price, p.profit
        FROM Persons p
        LEFT JOIN (
            SELECT color, MIN(model) AS model, MIN(price) AS price
            FROM Cars
            GROUP BY color
        ) c ON p.favorite_color = c.color AND c.price <= p.profit
        ORDER BY p.name ASC
    '''

    cursor.execute(query)

    print("name   model    color  price   profit")
    print("-----  -------  -----  ------  ------")
    for row in cursor.fetchall():
        person_name, model, color, price, profit = row
        print(f"{person_name} {model if model else 'NULL'} {color} {price if price else 'NULL'}  {profit}")

except sqlite3.Error as e:
    print(f"Error: {e}")

finally:
    conn.close()
