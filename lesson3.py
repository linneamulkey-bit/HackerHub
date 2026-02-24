#1 Import the randint() function from the random module
from random import randint
#2 Create two variables: set the number of tokens to 5 and the number of rounds to 0
tokens=10
rounds=0
#3 Create a while loop that runs so long as the user still has tokens (tokens > 0)
while tokens>0:
    print("You have "+str(tokens)+" tokens.")
    tokens=tokens-1
    rounds=rounds+1
    num1=randint(1,10)
    num2=randint(1,10)
    num3=randint(1,10)
    print(f"|{num1}|{num2}|{num3}|")
    if num1==num2 and num3==num1:
        temp=tokens
        tokens=tokens*2
        print("You have gained"+str(tokens-temp)+" tokens.")
    elif num1==num2 or num2==num3 or num1==num3:
        tokens=tokens+2
        print("You have gained 2 tokens.")
    else:
        tokens=tokens-1
        print("You have lost 1 tokens.")
    keepgoing=input("Do you want to keep playing and spend a token?")
    if keepgoing=="no":
        break
print("You played "+str(rounds)+" rounds.")
print("You ended with "+str(tokens)+" tokens.") 

#4 INSIDE LOOP: Tell the user how many tokens they have

#5 INSIDE LOOP: Decrement the user's tokens and increment the game's rounds

#6 INSIDE LOOP: Randomly generate three numbers between 1 and 10

#7 INSIDE LOOP: Create a set of conditional statements that double the user's tokens if all three numbers are the same, give the user 2 more tokens if two of the numbers are the same, and do nothing if  there are no matches

#8 INSIDE LOOP: Prompt the user if they want to spend another token to play another round; if so, use the continue statement; if not, use the break statement

#9 Finally, tell the user how many rounds they played