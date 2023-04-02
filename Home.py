import streamlit as st
from modules import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase you productivity.")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        # usuwamy element z session_state
        del st.session_state[todo]
        # reload session_state to reflect changes
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo",
              on_change=add_todo, key="new_todo")

# for inspection
# st.session_state
