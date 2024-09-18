import streamlit as st
import cfunctions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass

todos=  cfunctions.get_todos()

def add_todo():
    todo= st.session_state['web_newtodo']+"\n"
    todos.append(todo)
    cfunctions.write_todos(todos)

st.title("My Todo App")
st.subheader("Helps organise my daily activities")
st.write("I write to do tasks everyday")

for items in todos:
    st.checkbox(items)

st.text_input(label="",placeholder="Enter to do",on_change=add_todo,key='web_newtodo')
# st.text_input(label="",placeholder="Enter to do",onchange=add_todo(),key='web_newtodo')
