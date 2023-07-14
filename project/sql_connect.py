import mysql.connector


mydb=mysql.connector.connect(
host="localhost",
user="root",
password="",
database="mydatabase"
)

mycur=mydb.cursor()
mycur1=mydb.cursor()



