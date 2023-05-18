import streamlit as st
import functions

# Get list of tasks
tasks = functions.get_tasks()


# Add new task to list
def add_task():
    new_task = st.session_state['-NEW-TASK-'] + "\n"
    tasks.append(new_task)
    functions.write_tasks(tasks)


# Layout of items in app,
    # The order on the page correlates with the order they listed in this file
st.title("Task Master Web App")
st.subheader("Maximize your productivity")
st.write("Please select from the menu")


# Iterate through the list and create a checkbox for each item
for task in tasks:
    st.checkbox(task)


# Input box to add new task item
st.text_input(
    label="Add Task",
    label_visibility="collapsed",
    placeholder="Enter a new task",
    on_change=add_task,
    key='-NEW-TASK-'
)

