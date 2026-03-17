todos=["homework"]

options="""
1. View todos
2. Add a todo
3. Remove a todo
4. Save todo list
5. Exit"""

def display_options():
    print(options)

def view_todos():
    print(todos)

def add_todo():
    new=input("What would you like to add?")
    todos.append(new)

def remove_todo():
    delete=input("What do you want to remove?")
    todos.remove(delete)

def write_to_file():
    with open("todos.txt","w") as f:
        for todo in todos:
            f.write(todo+"\n")

while True:
    display_options()
    choice=input("What do you want to do?")
    if choice=="1":
        view_todos()
    if choice=="2":
        add_todo()
    if choice=="3":
        remove_todo()
    if choice=="4": 
        write_to_file()
    if choice=="5":
        break