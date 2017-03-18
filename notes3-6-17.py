#recursion-- think of as a tree; in below case branching twice at each level.
#can write fib such that it runs about as fast as the iterative counterpart

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#can we do this with lambda?

fib = lambda n: 1 if (n is 1 or n is 2) else fib(n-1) + fib(n-2)

#sick...

def sumto(n):
    if n == 1:
        return 1
    else:
        return n + sumto(n-1)

sumto = lambda n: 1 if n == 1 else n + sumto(n-1)

# recursive, as opposed to iterative

def exponent(base, power):
    if power == 0:
        return 1
    else:
        return base * exponent(base, power - 1)

exp = lambda x, y: 1 if y == 0 else x * exp(x, y - 1)

#is there a faster solution?

def exponent(base, power):
    if power == 0:
        return 1
    elif power % 2 == 0:
        return exponent(base, power / 2) * exponent(base, power / 2)
    else:
        return base * exponent(base, power - 1)

#make recursive sudoku checker and sudoku board
