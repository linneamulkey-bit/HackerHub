print("Welcome to my color guessing game! Here's how to play:")
print("First, choose whether you want to play with a friend or not")
print("Second, guess any one word color you want after the prompt 'Choose a color'")
print("Third, make sure your guess is all lowercase letters with no spaces")
print("Fourth, coninue guessing colors and follow the hints in all uppercase that appear along the way")
print("Fifth, once you have guessed all six colors, you win!")
print("Sixth, don't play the practice round")
print(" ")
print("The round is starting!")
tri=0
need=[]
guessed=[]
coloring=["mint","gold","coral","teal","charcoal","mustard"]
friend=input("Would you like to play with a friend?")
print(" ")
while len(coloring)>0:
    print(" ")
    colory=input("Choose a color.")
    if colory in coloring:
        print("CONGRATULATIONS! You have listed a color.")
        print(" ")
        guessed.append(colory)
        coloring.remove(colory)
        tri=tri+1
    elif colory not in coloring:
        print("Sorry, this color does not exist.")
        print(" ")
        tri=tri+1
    if friend=="yes":
        done=input("Write done after handing the computer to a friend.")
        print(" ")
        
    if "mint" in guessed and "color 1" in need:
        need.remove("color 1")
    if "gold" in guessed and "color 2" in need:
        need.remove("color 2")
    if "coral" in guessed and "color 3" in need:
        need.remove("color 3")
    if "teal" in guessed and "color 4" in need:
        need.remove("color 4")
    if "charcoal" in guessed and "color 5" in need:
        need.remove("color 5")
    if "mustard" in guessed and "color 6" in need:
        need.remove("color 6")
    if "mint" not in guessed and "color 1" not in need:
        need.append("color 1")
    if "gold" not in guessed and "color 2" not in need:
        need.append("color 2")
    if "coral" not in guessed and "color 3" not in need:
        need.append("color 3")
    if "teal" not in guessed and "color 4" not in need:
        need.append("color 4")
    if "charcoal" not in guessed and "color 5" not in need:
        need.append("color 5")
    if "mustard" not in guessed and "color 6" not in need:
        need.append("color 6")

    if tri==2 and "mint" in coloring:
        mint1=("HINT:COLOR 1 SMELLS AND TASTES GOOD. ")
        print(mint1)
    if tri==3 and "mint" in coloring:
        mint2=("HINT:COLOR 1 IS A TYPE OF GREEN. ")
        print(mint2)
    if tri==4 and "gold" in coloring:
        gold1=("HINT:COLOR 2 IS VALUBLE. ")
        print(gold1)
    if tri==5 and "gold" in coloring:
        gold2=("HINT:COLOR 2 IS SHINY. ")
        print(gold2)
    if tri==6 and "coral" in coloring:
        coral1=("HINT:COLOR 3 IS FOUND IN THE OCEAN. ")
        print(coral1)
    if tri==7 and "coral" in coloring:
        coral2=("HINT:COLOR 3 IS A TYPE OF ORANGE OR PINK. ")
        print(coral2)
    if tri==8 and "teal" in coloring:
        teal1=("HINT:COLOR 4 IS A TYPE OF BLUE. ")
        print(teal1)
    if tri==9 and "teal" in coloring:
        teal2=("HINT:COLOR 4 IS ALSO A TYPE OF GREEN. ")
        print(teal2)
    if tri==10 and "charcoal" in coloring:
        charcoal1=("HINT:COLOR 5 IS FOUND IN A FIRE. ")
        print(charcoal1)
    if tri==11 and "charcoal" in coloring:
        charcoal2=("HINT:COLOR 5 IS A TYPE OF BLACK. ")
        print(charcoal2)
    if tri==12 and "mustard" in coloring:
        mustard1=("HINT:COLOR 6 IS A CONDIMENT. ")
        print(mustard1)
    if tri==13 and "mustard" in coloring:
        mustard2=("HINT:COLOR 6 IS A KIND OF YELLOW. ")
        print(mustard2)

    if len(guessed)>0:
        print("You have guessed colors "+str(guessed))
    if len(need)>0:
        print("You need to guess "+str(need))

    if tri>3 and "color 1" in need:
        print("Remember the hints for color 1 are: "+str(mint1)+str(mint2))
    if tri>5 and "color 2" in need:
        print("The hints for color 2 are: "+str(gold1)+str(gold2))
    if tri>7 and "color 3" in need:
        print("The hints for color 3 are: "+str(coral1)+str(coral2))
    if tri>9 and "color 4" in need:
        print("The hints for color 4 are: "+str(teal1)+str(teal2))
    if tri>11 and "color 5" in need:
        print("The hints for color 5 are: "+str(charcoal1)+str(charcoal2))
    if tri>13 and "color 6" in need:
        print("The hints for color 6 are: "+str(mustard1)+str(mustard2))
else:
    print("All colors have been deleted. It took "+str(tri)+" tries.")
    print("Thanks for playing!")
    print(" ")
    print("Wierd broken practice round next. I wouldn't play it.")
    print(" ")
    practice=input("Would you like to play a practice round?")




if practice=="yes":
    person=input("Would you like to play with a friend?")
    colors=["red","yellow","green","blue","purple","pink","brown"]
    colors.append("orange")
    tries=0
    while len(colors)>0:
        color=input("Choose a color.")
        tries=tries+1
    if person=="yes":
        hand=input("Write done after handing the computer to a friend.")
    if color in colors:
        print("Congratulations! You have listed a color.")
        colors.remove(color)
    elif color not in colors:
        print("Sorry, this color does not exist.")
    if len(colors)==0:
        print("All colors have been deleted. It took "+str(tries)+" tries.")
        again=input("Do you want to play another round?")
    if again=="no":
        print("Thanks for playing!")