#Import librarys
from random import randint

#Declare and initialize variables and/or constants
player_lives = 3
dice1 = 0
dice2 = 0
roll_count = 0
equal_count = 0 
dices_add = 0
status = True

#Funtions
def rollDices ():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    return dice1, dice2

#Main
while status:
    dices = rollDices()
    roll_count +=1
    print(f"Roll dices N°: {roll_count}")
    print(f"Player lives: {player_lives}")
    print(f"Dice 1: {dices[0]}")
    print(f"Dice 2: {dices[1]}")
    dices_add = dices[0] + dices[1]

    if dices_add % 2 != 0:
        player_lives -=1
        print(f"You have lost one life::: Now you have {player_lives} lives")
        if player_lives == 0:
            print(":::Game over :::")
            break
    print(f"Dices addition: {dices_add}")

    if roll_count == 5:
        break
else:
    press_key = input ("\nPress any key to roll dices again")