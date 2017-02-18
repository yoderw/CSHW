from statistics import mean, stdev
from itertools import product
from math import erf, sqrt

# compute array of sums for possible dice rolls given n dice

def dice_sums_mean_stdev_list(n):
	x = product(range(6), repeat=n)
	y = [sum(i) for i in x]
	return [mean(y), stdev(y)]

#sums_dict = {i : dice_sums_mean_stdev_list(i) for i in range(4,14)}

# new approach:

mean = lambda n:(2.5 * n)
stdev = lambda n: sqrt(2.91 * n)
one_stdev_range = lambda m, s: (int(m - s), int(m + s))
two_stdev_range = lambda m, s: (int(m - (2 * s)), int(m + (2 * s)))
n_from_mean = lambda m: m / 2.5

range_dict = {i :  for i in range(4, 14)}