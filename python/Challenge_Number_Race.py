#Import librarys
from random import randint

# Declare and inizialite variables and/or constants 
dice1 = 0
dice2 = 0
status = True

#Funtions
def rollDices1 ():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    return dice1, dice2
def game ():
    print("Selected basic level\n :::GAME STARTS:::")
    key1 = input("Press Enter for throw the dices")
    return key1
def rollDices2(meta, players):
    
    # Positions of teh players
    Positions = [0] * players

    # Consecutive equal dices
    equal_dices = [0] * players

    winner = False 
    while winner == False:

        # Players turns
        for i in range(players):
            print(f":::Player {i + 1} Turn:::")

            dices = rollDices1()
            print(f"Dice 1: {dices[0]}")
            print(f"Dice 2: {dices[1]}")

            # Verify equal dices
            if dices[0] == dices[1]:
                equal_dices[i] +=1
                print("Equal dices!!")
            else:
                equal_dices[i] = 0

            # Win with 3 equal dices cosecutively
            if equal_dices[i] == 3:
                print(f"### Player {i + 1} wins ###")
                winner = True
                break

            # Move player
            movement = dices[0] + dices[1]
            Positions[i] += movement
            print(f"Your moviment:{movement} ")
            print(f"Your position: {Positions[i]}")     

            # Winner
            if Positions[i] >= meta:
                print(f":::Player {i + 1} wins:::")
                winner = True
                break
            
            input("Netx player....Press Enter")   

# Request the number of players
players = int(input("Enter the number of players \n(Minumun two, maximun four players) \n"))

if players < 2:
    print("You need more of two players for start the game ")
elif players > 4:
    print("Maximun four players please ")
else:

# Main menu
    while status:
        main_menu = print("""
Selec the boar level
[1] Basic level (20 position boar)
[2] Intermediate level (30 position boar)
[3] Advanced level (50 position boar)
[4] Expert level (100 position boar)
""")
        main_menu = int(input("Select any option: "))
        break  

# Game
    match main_menu: 
        case 1: 
            meta = 20
            game()
            rollDices2(meta, players)
        case 2: 
            meta = 30
            game()
            rollDices2(meta, players)
        case 3: 
            meta = 50
            game()
            rollDices2(meta, players)
        case 4: 
            meta = 100
            game()
            rollDices2(meta, players)
        case _:
            print("Invalid option")
