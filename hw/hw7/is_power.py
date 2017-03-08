def is_power(n, b):
    if n == 1:
        return True
    if n < 1:
        return False
    else:
        return is_power(n / b, b)
