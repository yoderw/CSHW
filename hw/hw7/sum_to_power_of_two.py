def sum_power2(n):
    if n == 0:
        return '1'
    if n == 1:
        return '(1+1)'
    else:
        return '(' + sum_power2(n-1) + '+' + sum_power2(n-1) + ')'
