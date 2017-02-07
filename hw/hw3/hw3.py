def sum_cubes(n):
	total = 0
	i = 1
	while i <= n:
		total += i ** 3
		i += 1
	return total

def is_prime(n):
	if n == 1:
		return False
	total = 0
	i = 1
	while i <= n:
		if n % i == 0:
			total += 1
		i += 1
	return total < 3

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

def digit(x, n):
	return 0 if (10 ** n) > x else (x % (10 ** (n + 1))) // (10 ** n)

def reverse(n):
	for i in range

def numpal(n):
	return n == reverse(n)
