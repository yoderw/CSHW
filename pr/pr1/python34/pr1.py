import random
import math
import pr1testing
random.seed()


def roll(): #function that rolls 1 6-sided die, returning an integer between 0 and 5
    return random.randint(0,5)

def play():
    player1 = input("Name of Player 1?")
    player2 = input("Name of Player 2?")
    score1 = 0
    score2 = 0
    last = False
    while True:
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print('It is', player1 + "'s turn.")
        numDice = int(input("How many dice do you want to roll?"))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice == 0:
            last = True
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print('It is', player2 + "'s turn.")
        numDice = int(input("How many dice do you want to roll?"))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True
    print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
    if score1 > 100:
        print(player2 + " wins.")
        return 2
    elif score2 > 100:
        print(player1 + " wins.")
        return 1
    elif score1 > score2:
        print(player1 + " wins.")
        return 1
    elif score2 > score1:
        print(player2 + " wins.")
        return 2
    else:
        print("Tie.")
        return 3

def autoplayLoud(strat1, strat2):
    score1 = 0
    score2 = 0
    last = False
    while True:

        print()
        print("Player 1: " + str(score1) + "   " + "Player 2: " + str(score2))
        print("It is Player 1's turn.")
        numDice = int(strat1(score1, score2, last))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print(numDice, " dice chosen.")
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice == 0:
            last = True

        print()
        print("Player 1: " + str(score1) + "   " + "Player 2: " + str(score2))
        print("It is Player 2's turn.")
        numDice = int(strat2(score2, score1, last))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print(numDice, " dice chosen.")
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True

    print("Player 1: " + str(score1) + "   " + "Player 2: " + str(score2))
    if score1 > 100:
        print("Player 2 wins.")
    elif score2 > 100:
        print("Player 1 wins.")
    elif score1 > score2:
        print("Player 1 wins.")
    elif score2 > score1:
        print("Player 2 wins.")
    else:
        print("Tie.")

def autoplay(strat1, strat2):
    score1 = 0
    score2 = 0
    last = False
    while True:

        numDice = int(strat1(score1, score2, last))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " " + str(d)
            i = i-1
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice == 0:
            last = True

        numDice = int(strat2(score2, score1, last))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            i = i-1
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True

    if score1 > 100:
        return 2
    elif score2 > 100:
        return 1
    elif score1 > score2:
        return 1
    elif score2 > score1:
        return 2
    else:
        return 3

def manyGames(strat1, strat2, n):
    player1Wins = 0
    player2Wins = 0
    ties = 0
    for i in range(n):
        if i % 2 == 0:
            result = autoplay(strat1, strat2)
        elif i % 2 != 0:
                
        result = autoplay(strat2, strat1)
        if result == 1:
            player1Wins += 1
        elif result == 2:
            player2Wins += 1
        else:
            ties += 1
    print("Player 1 Wins: ", player1Wins)
    print("Player 2 Wins: ", player2Wins)
    print("Ties: ", ties)


def sample1(myscore, theirscore, last):
    if myscore > theirscore:
        return 0
    else:
       return 12

def sample2(myscore, theirscore, last):
    #your code here
    return ___

def improve(strat1):
    #your code here
    return ___

def myStrategy(myscore, theirscore, last):
    #your code here
    return ___

#play()
