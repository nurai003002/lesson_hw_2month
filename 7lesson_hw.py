
# дз
import sqlite3

def create_connection(db_name):
    connection = sqlite3.connect(db_name)
    return connection

create_connection("hw.db")

def create_table(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql) 


# def dop_hw(conn):
#     sql = ("""SELECT * FROM  products WHERE mark > 100;""")
#     cursor = conn.cursor()
#     orders = cursor.execute(sql).fetchall()
#     print(orders)

def create_products(conn, product: tuple):
    sql = """INSERT INTO products
    (product_title, price, quantity)
    VALUES (?,?,?);

    """

    cursor = conn.cursor() 
    cursor.execute(sql, product)
    conn.commit()


def update_quantity(conn, id, new_quantity):
    sql = """UPDATE products SET quantity = ? WHERE id = ? """
    cursor = conn.cursor()
    cursor.execute(sql, (new_quantity, id))
    conn.commit()


def create_delete(conn, id: int):
    sql = """DELETE FROM products WHERE id = ?"""
    cursor = conn.cursor()
    cursor.execute(sql,(id,))
    conn.commit()  
    


sql_create_table = """
CREATE TABLE IF NOT EXISTS products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0
);
"""

connection = create_connection("hw.db")
if connection:
    print("Готово")
    create_table(connection, sql_create_table)
    create_delete(connection,5)
    create_delete(connection,4)
    update_quantity(connection, 2, 899)
    create_products(connection, ("paper", 99.55, 100))
    create_products(connection, ("apple", 23.00, 34))
    create_products(connection, ("cherry", 120.43, 5))


# доп.дз
import sqlite3
def min_products():
    connection = sqlite3.connect("hw.db")  
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM products WHERE price < 100")
    orders = cursor.fetchall()
    for order in orders:
        print(order)  
    cursor.close()
    connection.close()

min_products()
    
 