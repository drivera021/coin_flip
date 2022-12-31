import random

coin = ["H", "T"]
toss =  random.choice(coin)

def coin_toss(): 
    selection = str(input('Please select \"H\" for heads or \"T\" for tails:\n'))
    capital_selection = selection.upper()

    if capital_selection == toss:
            print("You guessed correctly! The coin landed on " + toss)
    else:
            print("You guessed incorrectly. The coin landed on " + toss)    

print("Welcome to Coin-Toss!\n")
coin_toss()





