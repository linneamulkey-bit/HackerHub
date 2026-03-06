todos=[]

options="""
1. View todos
2. Add a todo
3. Remove a todo"""

def display_options():
    print(options)
    choice=input("What do you want to do?")
    if choice=="1":
        view_todos()
    if choice=="2":
        add_todo()
    if choice=="3":
        remove_todo()

def view_todos():
    print(todos)

def add_todo():
    new=input("What would you like to add?")
    todos.append(new)

def remove_todo():
    delete=input("What do you want to remove?")
    todos.remove(delete)

display_options()