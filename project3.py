# ====================shop inventory project======================
import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    db = "shop"
)

# if(not conn):
#     print("not connected")
# else:
#     print("connected")    

cur = conn.cursor()
# query = "CREATE DATABASE IF NOT EXISTS shop"
# cur.execute(query)
query = "CREATE TABLE IF NOT EXISTS products(id int primary key, name varchar(30), price float, quantity int)"
cur.execute(query)
def add_product():
    id = int(input("Enter the id of the Product:"))
    name = input("Enter the name of product:")
    price = float(input("Enter the price of the Product:"))
    qty = int(input("Enter the quantity of the product:"))
    query = "INSERT INTO products values(%s,%s,%s,%s)"
    tup = (id,name,price,qty)
    cur.execute(query,tup)
# add_product()
# conn.commit()
def view_product():
    cur = conn.cursor()
    query = "SELECT * FROM products"
    cur.execute(query)
    res = cur.fetchall()
    for i in res:
        for j in i:
            print(j, end="\t")
        print("\n")  
# view_product()    
def update_product():
    cur = conn.cursor()
    id = int(input("For the updation of product, Enter id:"))
    sold = int(input("enter the sold quantiy of product:"))
    query = "UPDATE products set quantity = quantity - %s where id = %s " 
    tup = (sold,id)
    cur.execute(query,tup)
    # simple updation of products
    # c = "update products set quantity = 10 where id =2"
    # cur.execute(c)
# update_product()
conn.commit()

def delete_product():
    cur = conn.cursor()
    id = int(input("For the Deletion of product, Enter id:"))
    query = "DELETE FROM products where id = %s"
    tup =(id,)
    cur.execute(query,tup)

# delete_product()
conn.commit()
conn.close()    

