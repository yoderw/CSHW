def collatz_length(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + collatz_length(n // 2)
    else:
        return 1 + collatz_length((n * 3) + 1)

def remainder(n, d):
    if n == 0:
        return 0
    if n < 0:
        if n + d > 0:
            return d + n
        else:
            return remainder(n + d, d)
    if n > 0:
        if n + d < 0:
            return d - n
        else:
            return remainder(n - d, d)

def count_up_down(n):
    if n == 1:
        print(n)
    else:
        print(n)
        count_up_down(n - 1)
        print(n)

def is_power(n, b):
    if n == 1:
        return True
    if n < 1:
        return False
    else:
        return is_power(n / b, b)

def quotient(n, d):
    if n == 0:
        return 0
    if n < 0:
        if n + d > 0:
            return -1
        else:
            return -1 + quotient(n + d, d)
    if n > 0:
        if n - d < 0:
            return 0
        else:
            return 1 + quotient(n - d, d)

def reverse_of(xs):
    ys = xs[1:] + xs[:1]
    if ys[0] == xs[-1]:
        return ys
    else:
        reverse_of(ys)
