contacts={"Kara":15,"Vera":15,"Iyla":14,"Maggie":13}
options="""
1. View contacts
2. Add a contact
3. Remove a contact
4. Search for a contact
5. Exit
"""

def view_contacts():
    for key,value in contacts.items():
        print(f"{key}:{value}")

def add_contacts():
    add=input("Who would you like to add?")
    add_num=input("What is their phone number?")
    contacts[add]=add_num

def remove_contact():
    remove=input("Who's contact would you like to remove?")
    contacts.pop(remove)

def search():
    search=input("Who would you like to search for?")
    phone_num=(contacts[search])
    print(f"{search}:{phone_num}")

while True:
    print(options)
    do=int(input("What would you like to do?"))
    if do==1:
        view_contacts()
    if do==2:
        add_contacts()
    if do==3:
        remove_contact()
    if do==4:
        search()
    if do==5:
        break