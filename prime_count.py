from math import sqrt

values = [1000, 5000, 30000, 100000, 500000, 1000000, 2000000, 5000000, 10000000]

def is_prime(n):
	if n < 2:
		return False
	for i in range(2, int(sqrt(n) + 1)):
		if n % i == 0:
			return False
	return True

def sum_prime(n):
	total = 2
	for i in range(3, n, 2):
		if is_prime(i):
			total += i
	print("Sum of all primes below " + str(n) + ": " + str(total))

#for value in values:
#	sum_prime(value)

def prime_below(n):
	ls = [i for i in range(2,n)]
	for i in range(len(ls)):
		if ls[i]:
			for j in range(, len(ls), ls[i]):
				ls[j] = 0
	return ls
