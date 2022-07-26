import mysql.connector

mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     passwd='',
     database="ksiegarnia"
)

if mydb.is_connected():
     print("Successfully Connected")
else:
     print("Unsuccessfull Connected")

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM klienci where idklienta %2 = 0")

myresult = mycursor.fetchall()

for row in myresult:
     print(row)
	 
	 
	 #---------------------
	 