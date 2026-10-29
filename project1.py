
# ==================STUDENT MANAGEMENT SYSTEM ====================

import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    db = "student"
)

cur = conn.cursor()
query = "CREATE TABLE students(id int, name varchar(20), marks float)"
cur.execute(query)

# =======================INSERT manually data================
query = "INSERT INTO students values(1,'Sadia',95)"  #manually adding entries
cur.execute(query)
# =======================INSERT through tuples================
query = "INSERT INTO students values(%s,%s,%s)" #through the tuples
tup = (2,"shiza",85)
cur.execute(query,tup)
# =======================INSERT through the list of tuples======
query = "INSERT INTO students values(%s,%s,%s)" 
lst = [(3,"shenaz",95),(4,"sumbul",80)]
cur.executemany(query,lst)
"""
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    db = "student"
)

cur = conn.cursor()
# =====================Insert through input ===================== '''
id = int(input("enter your id:"))
name = input("enter your name:")
marks = float(input("enter your marks:"))
query = "INSERT INTO STUDENTS values(%s,%s,%s)"
tuple = (id,name,marks)
cur.execute(query,tuple)
conn.commit()
conn.close()
"""
query = "SELECT * from students where name = 'shiza'"
cur.execute(query)
res = cur.fetchall()
print(res)

query = "UPDATE students SET name='Ali', marks=89 where id=1"
cur.execute(query)
query = "DELETE from students where name = 'shiza'"
cur.execute(query)

# query = "DROP DATABASE student"
# cur.execute(query)

conn.commit()
conn.close()







