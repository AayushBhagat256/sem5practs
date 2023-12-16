import mysql.connector

mydb = mysql.connector.connect(
    user = 'root',
    password = '',
    host = 'localhost'
)

mycursor = mydb.cursor()

mycursor.execute("USE pythondb")

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
    
mycursor.execute("CREATE TABLE student(stuid INT PRIMARY KEY,sname VARCHAR(255))")

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
    
mycursor.execute("DESC student")
for x in mycursor:
    print(x)
    
"""
('student',)
('stuid', 'int(11)', 'NO', 'PRI', None, '')
('sname', 'varchar(255)', 'YES', '', None, '')
"""