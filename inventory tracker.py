options="""
1. View inventory
2. Add an item
3. Drop an item
4. Leave"""

inventory=[0]

def display_options():
    print(options)

def view_inventory():
    print(inventory)

def add_item():
    add=("What do you want to add?")
    inventory.append(add)

def drop_item():
    drop=("List the number of the item you want to drop")
    inventory.pop(drop)

while True:
    display_options()
    do=input("What do you want to do?")
    if do=="1":
        view_inventory()
    if do=="2":
        add_item()
    if do=="3":
        drop_item()
    if do=="4":
        break