from random import shuffle
catagories={"purple": ["a","b","c","d"],"yellow":["e","f","g","h"],"green":["i","j","k","l"],"blue":["m","n","o","p"]}
catagories_list=[["a","b","c","d"],["e","f","g","h"],["i","j","k","l"],["m","n","o","p"]]
guessed_purple=[]
guessed_blue=[]
guessed_yellow=[]
guessed_green=[]
 
def add(list,color):
    if guess1 in color:
        list.append(guess1)
    if guess2 in color:
        list.append(guess2)
    if guess3 in color:
        list.append(guess3)
    if guess4 in color:
        list.append(guess4)

shuffle(catagories_list)

while True:
    print("Choose four things in the list that you think go together and list them in the numbers below.")
    guess1=input("1.")
    guess2=input("2.")
    guess3=input("3.")
    guess4=input("4.")

    add(guessed_purple,"purple")
    add(guessed_yellow,"yellow")
    add(guessed_blue,"blue")
    add(guessed_green,"green")

    if len(guessed_blue)==4:
        print("Congratulations! You won!")
        break
    if len(guessed_green)==4:
        print("Congratulations! You won!")
        break
    if len(guessed_purple)==4:
        print("Congratulations! You won!")
        break
    if len(guessed_yellow)==4:
        print("Congratulations! You won!")
        break