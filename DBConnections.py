import pymysql

#function
def connectToDB():
    user = "sictc"
    password = "Pencil1"
    dbName = "IoT"
    host = "localhost"

    connection = pymysql.connect(
        database=dbName,
        user=user,
        password=password,
        host=host
    )
    #print(connection)
    #print(dir(connection))

    #mainloop
    try:
        if connection:
            print("Connected to the db")
    except pymysql.Error as e:
        print(f"Error while connecting to db: {e}")
        
connectToDB()