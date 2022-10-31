import streamlit as st
import sys
sys.path.append(".")
from DB_SQL_STREAMLIT_FUNCTIONS import total_lifted_for_exercise, total_lifted_for_exercise_in_date_range, all_instances_of_exercise_x, all_instances_of_exercise_x_in_date_range, plot_results, write_to_log

st.title('Main Page 🎉')
st.subheader("Here you can navigate to insert lifts and data to a database or interogate the database")