import psycopg2
from datetime import date

conn = psycopg2.connect(
    host='localhost', 
    user='root',
    password='YOUR_OWN_PASSWORD',
    database='MY_LIFTS'
    )

mycursor = conn.cursor()

mycursor.execute("CREATE TABLE `Lifts` (`Exercise_ID` int NOT NULL AUTO_INCREMENT,`Date_of_exercise` date NOT NULL, `Exercise` varchar(20) NOT NULL,`Sets` smallint NOT NULL, `Reps` smallint NOT NULL,`Weight` float NOT NULL,`Total_Reps` smallint NOT NULL,`Total_Load` float Not NULL,PRIMARY KEY (exercise_ID))")