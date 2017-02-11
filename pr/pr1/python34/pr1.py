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

# Recycled code from play(). 
# Takes as input two strategy functions and prints a game between them to the terminal.
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

# Recycled code from autoplayLoud() above. 
# The game loop is identical, all I did was remove the print statememts.
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

# Takes as input two strategy functions and an integer n.
# Uses a for-loop to iterate over range(n) and runs autoplay between the two functions for each iteration i
# If i is even, run autoplay(strat1, strat2), ie. strat1 plays first.
# If i is odd, run autoplay(strat2, strat1), ie. strat2 plays first.
def manyGames(strat1, strat2, n):
    player1Wins = 0
    player2Wins = 0
    ties = 0
    for i in range(n):
        if i % 2 == 0:
            result = autoplay(strat1, strat2)
            if result == 1:
                player1Wins += 1
            elif result == 2:
                player2Wins += 1
            else:
                ties += 1
        elif i % 2 != 0:      
            result = autoplay(strat2, strat1)
            if result == 1:
                player2Wins += 1
            elif result == 2:
                player1Wins += 1
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

# Straighforward, does nothing more than simple control flow.
def sample2(myscore, theirscore, last):
    if myscore <= 50:
        return 30
    elif 51 <= myscore <= 80:
        return 10
    else:
        return 0

# Takes as input a strategy function and returns an improved strategy function, new_strat().
# The new_strat() returns 0 if myscore is at least 100.
# Otherwise, it retuns strat1(myscore, theirscore, last), ie. does not augment behavior
def improve(strat1):
    def new_strat(myscore, theirscore, last):
        if myscore >= 100:
            return 0
        else:
            return strat1(myscore, theirscore, last)
    return new_strat

"""
After some consideration, I have begun to conceive of the game on a 2-3 turn model.
Ideally, a player would win on turn 2. They would roll n dice on turn 1,
where n would ensure their score be somewhere near or above 90 points.
On turn 2, they would know the n for each value 90-97 to roll.
Though ideal, the probabilistic nature of the game makes is seem unlikely that this could occur regularly.
This lead me to my 3 turn strategy- 
Turn 1: Roll 33 dice. (I think this is the ideal number to roll on turn 1, though I have not done the math)
Turn 2: Roll n dice, where n is calculated to put your score in the 90-97 range
Turn 3: Choose n using a predetermined ruleset (ie, assign an n value to each possible score)
I am going to attempt to use a normal distribution (bell curve) for the computation required in turn 2.
For turn 3, I will create some data structure with the values pre-computed for the predicted
score values (ie, 90-97).
Once I have done all that, I will begin to look into how I can take into account the opponent's score.
---
The idea is to have the function compute the bell curve for each n in range(x, y)
(x, y) is determined (somehow) from the input scores.
I am going to start by calculating the bell curve of n = (100 - myscore) // 3 dice, numbered 0-5.
I can determine the standard deviation of the normal distribution and return n +/- m dice,
where m is determined by the standard deviation. This variation would be determined by theirscore and last.
The total of n dice rolls will have a 68% chance of falling within 1 SD of the mean, 
a 95% chance of being w/in 2 SD of the mean
and a 99.7% chance of being w/in 3 SD of the mean.
Hopefully the range of these values will not be so great as to be impractical.
I will start with this basic functionality and iterate for later versions of the function.
---
I think I can use the numpy module to do most, if not all, of the heavy lifting.
"""
def myStrategy_mkI(myscore, theirscore, last):
    pass