# Print "Hello, World!"
print("Hello, world!")
# Create a variable holding your name. Then, print the value of the variable.

# Use the input() function to make the computer ask you for your name. Then, make the computer greet you.
name=input("What is your name?")
print("Hello "+str(name)+"!")
# Fun Project: Fortune Teller!

# 1) Use the input() function to ask the user if they want red, yellow, green, or blue.
color =input("Red, yellow, green, or blue?")
# 2) If they pick red, use the input() function to ask them if they want 1 or 2
if color=="red":
    numr == input("1 or 2?")
if numr == 1:
     print("Hey! You weren't supposed to pick this one!")
elif numr == 2:
    print("You will pet a pet.")
# 3) If they pick yellow, use the input() function to ask them if they want 3 or 4.
if color=="yellow":
    numy = int(input("3 or 4?"))
if numy == 3:
    print("The spirits are very happy today! They will do their best to shower everyone with good fortune!")
elif numy == 4:
    print("Have a great day "+str(name)+"!")
# 4) If they pick green, use the input() function to ask them if they want 5 or 6.
if color=="green":
    numg = int(input("5 or 6?"))
if numg == 5:
    print("Error fortune is not found. Good luck!")
elif numg == 6:
    print("You will read a book of Linnea's choice!")
# 5) If they pick blue, use the input() function to ask them if they want 7 or 8.
if color=="blue":
    numb = int(input("7 or 8?"))
if numb == 7:
    print("You will have a wonderfull year!")
elif numb == 8:
    print("You will live a long happy life!")
# 6) Depending on which number they pick, print out a different fortune!

# First, import the randint function from the random module
from random import randint
# Then, generate a random number between 1 and 10
randomnum=randint(1,1)
# Next, prompt the user for a number between 1 and 10
firstnum=int(input("Guess a number between 1 and 1,000!"))
if firstnum==randomnum:
    print("Congratulations, you won!")
while firstnum != randomnum:
    usernum=int(input("Incorrect."))
    if randomnum==usernum:
        print("Congratulations, you won!")
        break
    elif randomnum<usernum:
        print("Guess a lower number!")
    elif randomnum>usernum:
        print("Guess a higher number!")

# After, compare the user's number with the random number

# Finally, if the two numbers are the same, tell them they win the game. But if they are different, tell them they lost the game

# EXTENSION (just edit your code above!)

# Change the random number range from 1-10 to 1-100
# Create a while loop that runs until the user guesses the random number
# Inside the while loop, compare the user's guess with the random number — if the user guessed too high or too low, tell them that and prompt them for another number
# Exit the while loop once they guess correctly, and be sure to tell the user they won!