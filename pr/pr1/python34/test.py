from statistics import mean, stdev
from itertools import product
from math import erf

# compute array of sums for possible dice rolls given n dice

def dice_sums_list(n):
	x = product(range(6), repeat=n)
	y = [sum(i) for i in x]
	return tuple(y, mean(y), stdev(y))

sums_dict = {i : dice_sums_list(i) for i in range(14)]}