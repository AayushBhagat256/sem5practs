import mysql.connector 

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = ''
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE pythondb")

mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
    
"""
('college',)
('company',)
('fragmentation',)
('information_schema',)
('mysql',)
('optimise',)
('performance_schema',)
('phpmyadmin',)
('pythondb',) #ye dekh le
('test',)
"""