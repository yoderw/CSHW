# this solution runs in n^2 time
"""
def maxSublist(ls):
    contenders = {}
    for p1 in range(len(ls)):
        for p2 in range(p1, p1 + len(ls[p1:])):
            curr = ls[p1:p2 + 1]
            contenders[sum(curr)] = curr
    maxSub = max(contenders)
    return contenders.pop(maxSub)
"""

# this soution borrows conceptually from the linear solution for twoSum()
# worst case, it still runs in n^2 time. best/good case, runs in linear time
def maxSublist(ls):
    p1 = 0 # pointer1
    p2 = len(ls) # pointer2
    maxSub = ls
    i = 0
    while True:
        i += 1
        if p1 == p2:
            break
        if sum(ls[p1:p2]) > sum(maxSub):
            maxSub = ls[p1:p2]
        elif sum(ls[p1 + 1:p2]) > sum(ls[p1:p2 - 1]):
            p1 += 1
        elif sum(ls[p1:p2 - 1]) >= sum(ls[p1 + 1:p2]):
            p2 -= 1
        i += 1
    print(i)
    return maxSub


print(maxSublist([2,1,-3,4,-1,2,1,-5,4]))
