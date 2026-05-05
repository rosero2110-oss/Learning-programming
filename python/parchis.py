#import librarys
from random import randint

#Declare and initialize variables and/or constants
contador = 0 

#Funtions
def roll_dices():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    return dice1, dice2

#Main
while True:
    contador +=1
    dices = roll_dices()
    print(dices)
    print(f"dice 1: {dices[0]}")
    print(f"dice 2: {dices[1]}")
    print(f"numero de intentos: {contador}")
    if (dices[0] == dices[1]):
        print("You win")
        break
    else:
        print("Try again")
        key = input("Press any key to continue")
        