# this solution works in n^2 time
def longPalSub(s):
    ls = list(s)
    contenders = {}
    for p1 in range(len(ls)):
        for p2 in range(p1, p1 + len(ls[p1:])):
            sub = ls[p1:p2 + 1]
            rev = sub.copy()
            rev.reverse()
            if sub == rev:
                contenders[len(sub)] = "".join(sub)
    longPal = max(contenders)
    return contenders.pop(longPal)

# below is for checking
"""
print(longPalSub("cbcbaabaca")) #'baab'
print(longPalSub("cbcaa")) #'cbc'
"""
