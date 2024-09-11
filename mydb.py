import mysql.connector

dataBase = mysql.connector.connect(
  host='localhost',
  user='root',
  passwd = 'Virginmary@123#'

)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE antondom")

print("All Done!")
