import sqlite3
db = sqlite3.connect("data.db") # if the data base exists it will connect else it will create it
# run queries
db.execute("create table if not exists user_info (name text, age integer, address text)")
# close database
db.close()
#-----------------


db1 = sqlite3.connect("data1.db")
cr = db1.cursor()
cr.execute("create table if not exists users (user_id integer, name text)")
cr.execute("insert into users(user_id,name) values(1, 'ali')")
cr.execute("insert into users(user_id,name) values(2, 'ahmad')")
cr.execute("insert into users(user_id,name) values(3, 'noor')")

db1.commit()
 

 # we could have done it like this 
name_list= ["ali","numa","dia" ]
for key,user in enumerate(name_list):
    cr.execute(f"insert into users(user_id,name) values({key+1}, '{user}')")

cr.execute("select * from users")
print(cr.fetchone())
print(cr.fetchall())
