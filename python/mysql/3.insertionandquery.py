import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    password = '',
    user = 'root'
)

mycursor = mydb.cursor()

mycursor.execute("USE pythondb")

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
    
#query to insert
query = "INSERT INTO student (stuid,sname) VALUES (%s,%s)"
values = [
    (1,'Aayush'),
    (2,'messi'),
    (3,'ronaldo'),
]
mycursor.executemany(query,values)
mycursor.execute("SELECT * FROM student")
for x in mycursor:
    print(x)
    
# for single record
mycursor.execute("INSERT INTO student (stuid,sname) VALUES (4,'Virat')")
mycursor.execute("SELECT * FROM student")
for x in mycursor:
    print(x)

mycursor.execute("SELECT stuid from student where sname='Aayush'")
result = mycursor.fetchall()
for x in result:
    print(x)
    
query = "SELECT * from student where sname like %s"
param = [("%A%")]
mycursor.execute(query,param)
result = mycursor.fetchall()
for x in result:
    print(x)
print("---------------------------")
query = "DELETE FROM student WHERE stuid = 2"
mycursor.execute(query)
result = mycursor.fetchall()
for x in result:
    print(x)
mycursor.execute("SELECT * FROM student")
for x in mycursor:
    print(x)
