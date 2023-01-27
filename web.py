import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    toto = ""


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")


for index, todo_item in enumerate(todos):
    checkbox = st.checkbox(todo_item, key=todo_item)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo_item]
        st.experimental_rerun()

st.text_input(label="Add new todo",
              label_visibility='collapsed',
              placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

# st.session_state