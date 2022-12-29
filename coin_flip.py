import random

coin = ["H", "T"]
toss =  random.choice(coin)

selection = str(input('Please select \"H\" for heads or \"T\" for tails:\n'))
capital_selection = selection.upper()

def coin_toss(): 
    while capital_selection == ["H", "T"]:
        if capital_selection == toss:
            print("You guessed correctly! The coin landed on " + toss)
        else:
            print("You guessed incorrectly. The coin landed on " + toss)
        print('\n') 

print("Welcome to Coin-Toss!\n")
coin_toss()

#Wrong input
if capital_selection != ["H", "T"]:
    print("Selection not valid, please try again.")



