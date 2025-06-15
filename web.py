import streamlit as st 
"""pip install streamlit"""
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumurate(todos):
    st.checkbox(todo, key=todo)
"""Assign a signle name to each checkbox by its exact content, 
if key="value" it will make all checkboxes have the same key"""
    if checkbox:
        todos.pop(index) """remove if checked"""
        functions.write(todos)
        del st.session_state[todo] """delete from the dictionary after it was checked"""
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

print("Hello")

"""When deploying a Web app, you should have a streamlit app on a
 stand-alone python program, that means you shouldn't have unrelevant files"""