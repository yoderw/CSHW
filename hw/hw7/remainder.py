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
