import streamlit as st
import functions

tasks = functions.get_tasks(functions.FILEPATH)
new_task = functions.write_tasks(functions.FILEPATH)


st.title("Task Master Web App")
st.subheader("Maximize your productivity")
st.write("Please select from the menu")


for task in tasks:
    st.checkbox(task)


st.text_input(label="", placeholder="Enter a new task")


