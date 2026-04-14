import pymysql

#global stuff
user="sictc"
password="Pencil1"
dbName = "IoT"
host = "localhost"

connection = pymysql.connect(
    database=dbName,
    user=user,
    password=password,
    host=host
)
print(connection)
print(dir(connection))

#functions

#mainloop
