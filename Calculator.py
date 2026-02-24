def addition(num1,num2):
    print(f"{num1}+{num2}={num1+num2}")

def subtraction(num1,num2):
    print(f"{num1}-{num2}={num1-num2}")

def multiplication(num1,num2):
    print(f"{num1}*{num2}={num1*num2}")

def division(num1,num2):
    print(f"{num1}/{num2}={num1/num2}")

num1=int(input("Choose a first number."))
num2=int(input("Choose a second number."))
do=input("Would you like to add, subtract, multiply, or divide?")

if do=="add":
    addition(num1,num2)

if do=="subtract":
    subtraction(num1,num2)

if do=="multiply":
    multiplication(num1,num2)

if do=="divide":
    division(num1,num2)