# ======================== TODO LIST APP ========================

import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    db = "todo"
)
if(not conn):
    print("Database not connected")

cur = conn.cursor()
db = "CREATE DATABASE if not exists todo"
cur.execute(db)

tb = "CREATE TABLE IF NOT EXISTS tasks(id int primary key, task VARCHAR(20),status VARCHAR(20))"
cur.execute(tb)
# ======= add the task into tasks_Table =====
def add_task():
    cur = conn.cursor()
    id = int(input("enter the task id:"))
    task = input("enter task name:")
    status = "pending"
    add = "INSERT INTO tasks values(%s,%s,%s)"
    tup = (id,task,status)
    cur.execute(add,tup)
# add_task()  
conn.commit() 
# ======= view the tasks from tasks_table =====
def view_task():
    cur = conn.cursor()
    query = "SELECT * FROM tasks"
    cur.execute(query)
    res = cur.fetchall()
    for i in res:
        for j in i:
            print(j, end= "\t")
        print("\n")    
# view_task()
# ======= Updat task pending to done =====
def update_task():
    cur = conn.cursor()
    id = int(input("enter id of done task:"))
    query = "UPDATE tasks set status = 'Done' where id = %s"
    tup  = (id,)
    cur.execute(query,tup)
    
# update_task()
conn.commit()
def delete_task():
   cur = conn.cursor()
   id = int(input("Enter Id for deletion of the task:"))
   query = "DELETE from tasks where id = %s " 
   tup = (id,)
   cur.execute(query,tup)
delete_task()
conn.commit()   
conn.close()
