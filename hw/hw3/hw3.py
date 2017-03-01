from math import sqrt

def sum_cubes(n):
	total = 0
	for i in range(n):
		total += (i + 1) ** 3
	return total

def is_prime(n):
	if n < 2:
		return False
	for i in range(2, int(sqrt(n) + 1)):
		if n % i == 0:
			return False
	return True

def fib(n):
	a, b = 0, 1
	for i in range(n - 1):
		b, a = b + a, b
	return b

def fib3(n):
	a, b, c = 0, 0, 1
	for i in range(n - 1):
		c, b, a = c + b + a, c, b
	return c

def pyramid(h):
	string = ''
	for i in range(h):
		string += (" " * (h - (i + 1)) + ("* " * i) + "*" + "\n")
	return string

def collatz(n):

	def seq_len(m):
		i = 1
		while m != 1:
			m = m // 2 if m % 2 == 0 else (m * 3) + 1
			i += 1
		return i

	i = 1
	while True:
		if seq_len(i) >= n:
			return i
		else:
			i += 1

def numpal(n):

	def digit(n, x):
		return None if (10 ** x) > n else (n % (10 ** (x + 1))) // (10 ** x)

	def int_len(n):
		i = 0
		while True:
			if digit(n, i) is None:
				return i
			else:
				i += 1

	def reverse(n):
		out = 0
		for i in range(0, int_len(n)):
			out += digit(n, i) * (10 ** ((int_len(n) - 1) - i))
		return out

	return n == reverse(n)

def poly2max(x1, x2, y1, y2):
	poly = lambda x, y: -x**4 + 3*x**2 - y**4 + 5*y**2
	values = [poly(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]
	return max(values)

"""
def solve(a, b, c):
	disc = b**2 - 4*a*c
	if disc >= 0 and sqrt(disc) == int(sqrt(disc)):
		x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
		x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
		if int(x1) == x1 and int(x2) == x2:
			return int(max(x1, x2))
	return False
"""

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def solve(a, b, c):
	disc = b**2 - 4*a*c
	div = 2*a
	x1 = (-b + isqrt(disc))
	x2 = (-b - isqrt(disc))
	if disc >= 0:
		if isqrt(disc) == sqrt(disc):
			if not x1 % div and not x2 % div:
				return max(x1 // div, x2 // div)
			elif x1 % div and not x2 % div:
				return x2 // div
			elif not x1 % div and x2 % div:
				return x1 // div
	return False

