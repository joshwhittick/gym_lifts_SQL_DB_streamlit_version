import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Kayak:27"
)

mycursor = mydb.cursor()

mycursor.open("gym_lifts_tracking")