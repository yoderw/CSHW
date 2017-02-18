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

# returns 4 if loss of my strat was due to overshoot
def autoplay_mod(strat1, strat2):
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
        return 2, True
    elif score2 > 100:
        return 1, True
    elif score1 > score2:
        return 1, False
    elif score2 > score1:
        return 2, False
    else:
        return 3, False

def manyGames_mod(strat1, strat2, n):
    player1Wins = 0
    player2Wins = 0
    p1_over = 0
    p2_over = 1
    ties = 0
    for i in range(n):
        if i % 2 == 0:
            result = autoplay_mod(strat1, strat2)
            if result[0] == 1:
                if result[1]:
                    p2_over += 1
                player1Wins += 1
            elif result[0] == 2:
                if result[1]:
                    p1_over += 1
                player2Wins += 1
            else:
                ties += 1
        elif i % 2 != 0:
            result = autoplay_mod(strat2, strat1)
            if result[0] == 1:
                if result[1]:
                    p1_over += 1
                player2Wins += 1
            elif result[0] == 2:
                if result[1]:
                    p2_over += 1
                player1Wins += 1
            else:
                ties += 1
    print("Player 1 Wins: ", player1Wins)
    print("Player 2 Wins: ", player2Wins)
    print("Ties: ", ties)
    print("p1 overshoots: ", p1_over)
    print("p2 overshoots: ", p2_over)

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

from math import sqrt
from pr1testing import test11 as std

# mean(n) := return the mean of the normal distribution of dice total d
mean = lambda d: 2.5 * d

# stdev(m) := return the standard deviation of mean m
stdev = lambda m: sqrt(2.91 * m)

# range1(m, s) := return an iterable of the range of integer values within one stdev s of mean m
range1 = lambda m, s: range(int(m - s), int(m + s) + 1)

# range2(m, s) := return an iterable of the range of integer values within two stdev s of mean m
range2 = lambda m, s: range(int(m - (2 * s)), int(m + (2 * s) + 1))

# n_from_mean(m) := return the dice total having normal distribution with mean m
d_from_mean = lambda m: m / 2.5

# dict comp containing the ranges of 1 and 2 standard deviations from the mean as values,
# and the number of associated dice as values, calculated using the above functions.
range_dict = {i : [range1(mean(i), stdev(mean(i))), range2(mean(i), stdev(mean(i)))] for i in range(1, 15)}

# below is the output of the dict compt with some augmented values
range_dict = {1: [range(0, 6), range(0, 8)],
              2: [range(1, 9), range(0, 13)],
              3: [range(2, 13), range(0, 17)],
              4: [range(4, 16), range(0, 21)],
              5: [range(6, 19), range(0, 25)],
              6: [range(8, 22), range(1, 29)],
              7: [range(10, 25), range(3, 32)],
              8: [range(12, 28), range(4, 36)],
              9: [range(14, 31), range(6, 39)],
              10: [range(16, 34), range(7, 43)],
              11: [range(18, 37), range(9, 46)],
              12: [range(20, 40), range(11, 49)],
              13: [range(22, 43), range(13, 52)],
              14: [range(24, 46), range(14, 56)]
              }

def range_dict_sort(diff, dict=range_dict):
    empty = lambda ls: True if len(ls) == 0 else False
    aggr = []
    safe = []
    for i in dict:
        if diff in dict[i][0]:
            aggr.append(i)
        elif diff in dict[i][1]:
            safe.append(i)
    return [x[0] for x in (aggr, safe) if not empty(x)]

def myStrategy(myscore, theirscore, last):
    return myStrategy_mkIII(myscore, theirscore, last)

def myStrategy_template(myscore, theirscore, last):
    # diff := the difference between 100 and myscore
    # thresh1/2 := threshholds of point values at which the strategy will change tactics; mainly for sake of testing.
    diff = 100 - myscore
    thresh1 = 50
    thresh2 = 80
    thresh3 = 97

    # range_dict may change with version.
    # will keep default as the global for testing purposes until I feel the need to change
    global range_dict

    # range_sort(x, y, z) := given diff x and parameter y, sort dict z
    def range_dict_sort(x, y, z):
        pass

    # below_threshx := the sub-function to be used when myscore <= threshx
    def below_thresh1(myscore, theirscore, last):
        return 33

    def below_thresh2(myscore, theirscore, last):
        pass

    def below_thresh3(myscore, theirscore, last):
        pass

    # basic control flow of the strategy:
    if diff <= thresh1:
        return below_thresh1(myscore, theirscore, last)

    elif thresh1 < diff <= thresh2:
        return below_thresh2(myscore, theirscore, last)

    elif thresh2 < diff <= thresh3:
        return below_thresh3(myscore, theirscore, last)

    else:
        return 0

# first iteration of the above template; wins consistently against the first 7 strategies, with a small margin of difference against the last 3
def myStrategy_mkI(myscore, theirscore, last):
    # diff := the difference between 100 and myscore
    diff = 100 - myscore

    # thresh1/2/3 := threshholds of point values at which the strategy will change tactics; mainly for sake of testing.
    thresh1 = 60
    thresh2 = 89
    thresh3 = 97

    # global is for tesing purposes only
    global range_dict

    # range_sort(x, y, z) := given diff x and parameter y, sort dict z
    # below is temp; proof of concept
    def range_dict_sort(diff=diff, dict=range_dict):
        empty = lambda ls: True if len(ls) == 0 else False
        aggr = []
        safe = []
        for i in dict:
            if diff in dict[i][0]:
                aggr.append(i)
            elif diff in dict[i][1]:
                safe.append(i)
        return [x[0] for x in (aggr, safe) if not empty(x)]


    # below_threshx := the sub-function to be used when myscore <= threshx
    def below_thresh1(myscore, theirscore, last):
        return diff // 3

    def below_thresh2(myscore, theirscore, last):
        if myscore < theirscore:
            return range_dict_sort()[0]
        elif myscore >= theirscore:
            return range_dict_sort()[1]

    def below_thresh3(myscore, theirscore, last):
        if last and myscore == theirscore and theirscore in range(97, 100):
            return 0
        else:
            return (diff // 6) + 1
    
    # the basic control flow of the strategy:
    if myscore <= thresh1:
        return below_thresh1(myscore, theirscore, last)
    elif thresh1 < myscore <= thresh2:
        return below_thresh2(myscore, theirscore, last)
    elif thresh2 < myscore <= thresh3:
        return below_thresh3(myscore, theirscore, last)
    else:
        return 0

# below beats 1-10 as is, with small margin of difference in test11
def myStrategy_mkII(myscore, theirscore, last):
    # diff := the difference between 100 and myscore
    diff = 100 - myscore

    # thresh1/2/3 := threshholds of point values at which the strategy will change tactics; mainly for sake of testing.
    thresh1 = 60
    thresh2 = 89
    thresh3 = 96

    # global is for testing purposes only
    global range_dict

    # below is temp; proof of concept
    def range_dict_sort(diff=diff, dict=range_dict):
        empty = lambda ls: True if len(ls) == 0 else False
        aggr = []
        safe = []
        for i in dict:
            if diff in dict[i][0]:
                aggr.append(i)
            elif diff in dict[i][1]:
                safe.append(i)
        return [x[0] for x in (aggr, safe) if not empty(x)]


    # below_threshx := the sub-function to be used when myscore <= threshx
    def below_thresh1(myscore, theirscore, last):
        return diff // 3

    def below_thresh2(myscore, theirscore, last):
        if myscore < theirscore:
            return range_dict_sort()[0]
        elif myscore >= theirscore:
            return range_dict_sort()[1]

    def below_thresh3(myscore, theirscore, last):
        return (diff // 6) + 1

    def above_thresh3(myscore, theirscore, last):
        if myscore >= theirscore:
            return 0
        if myscore < theirscore:
            return 1

    # the basic control flow of the strategy:
    if myscore <= thresh1:
        return below_thresh1(myscore, theirscore, last)
    elif thresh1 < myscore <= thresh2:
        return below_thresh2(myscore, theirscore, last)
    elif thresh2 < myscore <= thresh3:
        return below_thresh3(myscore, theirscore, last)
    elif thresh3 < myscore:
        return above_thresh3(myscore, theirscore, last)
    else:
        return 0

def myStrategy_mkIII(myscore, theirscore, last):
    # diff := the difference between 100 and myscore
    diff = 100 - myscore

    # thresh1/2/3 := threshholds of point values at which the strategy will change tactics; mainly for sake of testing.
    thresh1 = 60
    thresh2 = 89
    thresh3 = 96

    # global is for testing purposes only
    global range_dict

    # below is temp; proof of concept
    def range_dict_sort(diff=diff, dict=range_dict):
        empty = lambda ls: True if len(ls) == 0 else False
        aggr = []
        safe = []
        for i in dict:
            if diff in dict[i][0]:
                aggr.append(i)
            elif diff in dict[i][1]:
                safe.append(i)
        return [x[0] for x in (aggr, safe) if not empty(x)]


    # below_threshx := the sub-function to be used when myscore <= threshx
    def below_thresh1(myscore, theirscore, last):
        return diff // 3

    def below_thresh2(myscore, theirscore, last):
        if myscore < theirscore:
            return range_dict_sort()[0]
        elif myscore >= theirscore:
            return range_dict_sort()[1]

    def below_thresh3(myscore, theirscore, last):
        return (diff // 6) + 1

    def above_thresh3(myscore, theirscore, last):
        if myscore >= theirscore:
            return 0
        if myscore < theirscore:
            return 1

    # the basic control flow of the strategy:
    if myscore <= thresh1:
        return below_thresh1(myscore, theirscore, last)
    elif thresh1 < myscore <= thresh2:
        return below_thresh2(myscore, theirscore, last)
    elif thresh2 < myscore <= thresh3:
        return below_thresh3(myscore, theirscore, last)
    elif thresh3 < myscore:
        return above_thresh3(myscore, theirscore, last)
    else:
        return 0

test = lambda: pr1testing.testStrat(myStrategy, 10000)

def big_data():
    for i in range(80, 101):
        for j in range(80, 101):
            if myStrategy(i, j, 0) != std(i, j, 0):
                print()
                print("i:{} j{}".format(i, j))
                print("myOut:{}, theirOut:{}".format(myStrategy(i,j,0), std(i,j,0)))