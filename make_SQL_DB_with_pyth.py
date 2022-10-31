import psycopg2
from datetime import date

conn = psycopg2.connect(
    host='ec2-54-228-125-183.eu-west-1.compute.amazonaws.com', 
    user='clokjbklnxevbe',
    password='1211673e1d579c5db019e37f1ce28b2894f5d0f8b14415dc82c116e725562442',
    database='d91nc5sad12f6v',
    port='5432')

mycursor = conn.cursor()

mycursor.execute("CREATE TABLE Lifts (Exercise_ID serial NOT NULL, Date_of_exercise date NOT NULL, Exercise varchar(20) NOT NULL, Sets smallint NOT NULL, Reps smallint NOT NULL, Weight float NOT NULL, Total_Reps smallint NOT NULL, Total_Load float NOT NULL, PRIMARY KEY (Exercise_ID))")