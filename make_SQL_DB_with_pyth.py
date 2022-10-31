import psycopg2
from datetime import date

conn = psycopg2.connect(
    host=st.secrets["host"], 
    user=st.secrets["user"],
    password=st.secrets["password"],
    database=st.secrets["database"],
    port=st.secrets["port"])

mycursor = conn.cursor()

mycursor.execute("CREATE TABLE Lifts (Exercise_ID serial NOT NULL, Date_of_exercise date NOT NULL, Exercise varchar(20) NOT NULL, Sets smallint NOT NULL, Reps smallint NOT NULL, Weight float NOT NULL, Total_Reps smallint NOT NULL, Total_Load float NOT NULL, PRIMARY KEY (Exercise_ID))")

conn.commit()