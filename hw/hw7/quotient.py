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
