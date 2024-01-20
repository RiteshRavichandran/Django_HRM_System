import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "ritesh2002"

)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database 
cursorObject.execute("CREATE DATABASE simplify3x")

print("DATABASE created sucessfuly!")