import psycopg2
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
import numpy as np
import streamlit as st
from datetime import date

conn = psycopg2.connect(
    host=st.secrets["host"], 
    user=st.secrets["user"],
    password=st.secrets["password"],
    database=st.secrets["database"],
    port=st.secrets["port"])

mycursor = conn.cursor()

#function for writing data to DB
def write_to_log(date, lift, lift_sets, lift_reps, lift_load, total_reps, total_load):
  mycursor.execute("INSERT INTO Lifts (Date_of_exercise, Exercise, Sets, Reps, Weight, Total_Reps, Total_Load) VALUES (%s, %s, %s, %s, %s, %s, %s)", (date, lift, lift_sets, lift_reps, lift_load, total_reps, total_load))
  conn.commit()

def total_lifted_for_exercise(exercise_X):
    mycursor.execute("SELECT SUM(Total_Load) FROM Lifts WHERE Exercise='%s' " % exercise_X)
    myresult = mycursor.fetchall()

    st.text("The total lifted for %s is:" % exercise_X)
    for x in myresult:
      st.text(x)
  
def total_lifted_for_exercise_in_date_range(exercise_X):

    start_date = st.text_input("Start date (YYYY-MM-DD): ")
    end_date = st.text_input("End date (YYYY-MM-DD): ")
    if end_date != "":
      mycursor.execute("SELECT SUM(Total_Load) FROM Lifts WHERE Exercise='%s' AND Date_of_exercise between '%s' and '%s' " % (exercise_X, start_date, end_date))
      myresult = mycursor.fetchall()

      st.text("The total lifted for %s is:" % exercise_X)
      for x in myresult:
        st.text(x)

# no date range - all data for an exercise
def all_instances_of_exercise_x(exercise_X):

  mycursor.execute("SELECT * FROM Lifts WHERE Exercise='%s' " % exercise_X)
  myresult = mycursor.fetchall()
  
  for row in myresult:
    Exersise_ID = row[0]
    Date_of_exercise = row[1]
    Exercise = row[2]
    Sets = row[3]
    Reps = row[4]
    Weight = row[5]
    Total_Reps = row[6]
    Total_Load = row[7]
    st.write('{Exercise} on {Date_of_exercise} for {Sets} sets and {Reps} reps (total reps:{Total_Reps}) with {Weight} kgs = total load: {Total_Load}'.format(
      Date_of_exercise = Date_of_exercise, Exercise = Exercise, Sets = Sets, Reps = Reps, Weight = Weight, Total_Reps = Total_Reps, Total_Load = Total_Load))
  return myresult

# with date range - all data for an exercise
def all_instances_of_exercise_x_in_date_range(exercise_X):

  start_date = st.text_input("Start date (YYYY-MM-DD): ")
  end_date = st.text_input("End date (YYYY-MM-DD): ")
  
  if end_date != "":
    mycursor.execute("SELECT * FROM Lifts WHERE Exercise='%s' AND Date_of_exercise between '%s' and '%s' " % (exercise_X, start_date, end_date))
    myresult = mycursor.fetchall()
  
  for row in myresult:
    Exersise_ID = row[0]
    Date_of_exercise = row[1]
    Exercise = row[2]
    Sets = row[3]
    Reps = row[4]
    Weight = row[5]
    Total_Reps = row[6]
    Total_Load = row[7]
    st.write('{Exercise} on {Date_of_exercise} for {Sets} sets and {Reps} reps (total reps:{Total_Reps}) with {Weight} kgs = total load: {Total_Load}'.format(
        Date_of_exercise = Date_of_exercise, Exercise = Exercise, Sets = Sets, Reps = Reps, Weight = Weight, Total_Reps = Total_Reps, Total_Load = Total_Load))
  return myresult

# plot results from selected data
def plot_results(x):
  dates = []
  sets = []
  reps = []
  load = []
  total_reps = []
  total_lifted = []

  for row in x:
    dates.append(row[1])
    sets.append(row[3])
    reps.append(row[4])
    load.append(row[5])
    total_reps.append(row[6])
    total_lifted.append(row[7])
  fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
  ax1.plot(dates, total_reps)
  ax2.plot(dates, total_lifted)
  ax3.plot(dates, load)
  plt.xlabel("Date")
  plt.xticks(dates, rotation = 45)
  ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
  ax1.set_ylabel("Total reps")
  ax2.set_ylabel("Total lifted")
  ax3.set_ylabel("Load used")
  plt.show()
  st.write(fig)

