print("Welcome to my through the greenglass door game!")
print("The instructions for this game are:")
print("One, guess a word in all lowercase and no spaces when prompted.")
print("Two, use your FOUR hints when you want.")
print("Three, make a guess of what the pattern is if you have a guess. If you guess right, you win!")
print("Four, please respond to any question that is a yes or no question with yes or no")
print(" ")

win=""
hints=["Think about the letters.","Are there any interesting letters next to each other?","This can happen multiple times in a word.","Sometimes letters work well in pairs."]
letters=["aa","bb","cc","dd","ee","ff","gg","hh","ii","jj","kk","ll","mm","nn","oo","pp","qq","rr","ss","tt","uu","vv","ww","xx","yy","zz"]

while win!="A":
    word=input("Guess a word!")
    if any(double in word for double in letters):
         print(f"Yes, {word} can go through the greenglass door!")
         print(" ")
    else:
         print(f"Sorry, {word} cannot go through the greenglass door.")
         print(" ")
    
    hint=input("Do you want a hint?")
    if hint=="yes" and len(hints)==0:
         print("Sorry, you're all out of hints!")
         print(" ")
    if hint=="yes" and len(hints)>0:
         print(hints[0])
         hints.pop(0)
         print(" ")
    else:
         print(" ")
    
    guess=input("Would you like to make a guess about the pattern?")
    print(" ")
    if guess=="no":
         continue
    if guess=="yes":
         win=input("Do you think it's" \
        " A: double letters." \
        " B: two or more vowels." \
        " C: double vowels." \
        " D: three or more letters.")
    if win=="A":
         print("Congratulations! You win!")
    else:
         print("Sorry, that wasn't right. Keep on guessing words to figure it out!")
         print(" ")