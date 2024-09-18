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

for items ,todo in enumerate(todos):
    checkbox_value = st.checkbox(todo,key=todo)
    if  checkbox_value:
        todos.pop(items)
        cfunctions.write_todos(todos)
        del st.session_state[todo]
      # st.experimental_rerun() #not working in streamlit 1.38 not able to downgrade to 1.37

st.text_input(label=" ",placeholder="Enter to do",on_change=add_todo,key='web_newtodo')

#to show the session state
#st.session_state