catagories={"purple":["[a]","[b]","[c]","[d]"],"yellow":["[e]","[f]","[g]","[h]"],"green":["[i]","[j]","[k]","[l]"],"blue":["[m]","[n]","[o]","[p]"]}
guessed=[]

print("Choose four things in the list that you think go together and list them in the numbers below.")
guess1=input("1.")
guess2=input("2.")
guess3=input("3.")
guess4=input("4.")
   
def add(color):
    if guess1 in color:
        guessed.append(guess1)
    if guess2 in color:
        guessed.append(guess2)
    if guess3 in color:
        guessed.append(guess3)
    if guess4 in color:
        guessed.append(guess4)


