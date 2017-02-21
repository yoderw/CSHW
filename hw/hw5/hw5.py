from math import sqrt

def down_up(n):
	ls = [1]
	for i in range(1,n):
		ls.insert(0,i+1)
		ls.append(i+1)
	return ls

def filter(test, xs):
	ls = []
	for i in xs:
		if test(i):
			ls.append(i)
	return ls

def make_even(xs):
	odd = lambda n: n % 2 != 0
	for i in range(len(xs)):
		if odd(xs[i]):
			xs[i] -= 1

def char_count(s):
	ds = {}
	for char in s:
		if char in ds:
			ds[char] += 1
		else:
			ds[char] = 1
	return ds

def counts(n, xs):
	ls = [0 for i in range(n)]
	for i in xs:
		ls[i] += 1
	return ls

def is_prime(n):
	if n < 2:
		return False
	for i in range(2, int(sqrt(n) + 1)):
		if n % i == 0:
			return False
	return True

def primes_list(n):
	ls = []
	i = 2
	while True:
		if len(ls) == n:
			break
		elif is_prime(i):
			ls.append(i)
		i += 1
	return ls

def has_duplicates(xs):
	for i in xs:
		if xs.count(i) > 1:
			return True
	return False

def inverse(d):
	xd = {}
	for k in d:
		if d[k] in xd:
			xd[d[k]].append(k)
		else:
			xd[d[k]] = [k]
	return xd