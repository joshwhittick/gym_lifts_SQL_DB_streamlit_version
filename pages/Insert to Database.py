import streamlit as st
import sys
sys.path.append(".")
from DB_SQL_STREAMLIT_FUNCTIONS import total_lifted_for_exercise, total_lifted_for_exercise_in_date_range, all_instances_of_exercise_x, all_instances_of_exercise_x_in_date_range, plot_results, write_to_log

st.markdown("# Insert to Database")

date = st.text_input("Enter a date of gym session (YYYY-MM-DD):")
st.caption("Enter values for all exercises perfomed that day top enter and then commit to DB")

with st.form("insert vallues for lift", clear_on_submit=True):
  lift = st.text_input("enter lift")
  sets = st.number_input("enter sets")
  reps = st.number_input("enter reps")
  load = st.number_input("enter load")
  total_reps = sets * reps
  total_load = load * sets * reps
  if st.form_submit_button() == True:
    st.text("Data commited to DB")
    write_to_log(date, lift, sets, reps, load, total_reps, total_load)