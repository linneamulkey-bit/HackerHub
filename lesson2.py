# First, import the randint function from the random module
from random import randint
# Then, generate a random number between 1 and 10
randomnum=randint(1,20)
# Next, prompt the user for a number between 1 and 10
firstnum=int(input("Guess a number between 1 and 20!"))
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