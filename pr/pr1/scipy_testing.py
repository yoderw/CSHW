from numpy.polynomial.polynomial import polypow
from numpy import ones
 
sides = 6
dice = 3
 
# Create an array of polynomial coefficients for
# x + x^2 + ... + x^sides
p = ones(sides + 1)
p[0] = 0
p /= sides
pmf = polypow(p, dice)
cdf = pmf.cumsum()