import time
FILEPATH="todos.txt"

def get_todos(file_path_local=FILEPATH):
    """ Docstrings reads a text file
    and returns the value as a list
    """
    with open(file_path_local, 'r') as file1_local:
        todos_local = file1_local.readlines()
    return todos_local


def write_todos(todos_local,file_path_local=FILEPATH):
    """
    Writes the list contents to the file
    """
    with open(file_path_local, 'w') as file1_local:
        file1_local.writelines(todos_local)


def get_date():
    str = time.strftime("%d %B %Y")
    return (str)

