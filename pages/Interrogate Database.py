import streamlit as st
import sys
sys.path.append(".")
from DB_SQL_STREAMLIT_FUNCTIONS import total_lifted_for_exercise, total_lifted_for_exercise_in_date_range, all_instances_of_exercise_x, all_instances_of_exercise_x_in_date_range, plot_results, write_to_log

st.markdown("# Interogate Database")
st.title("Interogate Lifting Database")

st.text("1: See all time total weight lifted for an exercise.\n2: See all the days and associated sets/reps/load for an exercise.")
options = st.radio('Pick query option:', ('1', '2'))
 
if options == "1":
  with st.form("Enter values", clear_on_submit=True):
    lift = st.text_input("What lift do you want to see the sum of all weight lifted for?")
    daterange_option = st.text_input("Do you need a date range? (y/n)")
    if st.form_submit_button() == True:
      if daterange_option == "n":
        total_lifted_for_exercise(lift)
      elif daterange_option == "y":
        total_lifted_for_exercise_in_date_range(lift)

if options == "2":
  with st.form("Enter values", clear_on_submit=True):
    lift = st.text_input("What lift do you want to see all data for?")
    daterange_option = st.text_input("Do you need a date range? (y/n)")
    if st.form_submit_button() == True:
      if daterange_option == "n":
        plot_results(all_instances_of_exercise_x(lift))
      elif st.form_submit_button() == True and daterange_option == "y":
        plot_results(all_instances_of_exercise_x_in_date_range(lift))
