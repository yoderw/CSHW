# this solution runs in linear time on sorted lists
"""
def twoSum(ls, n):
    p1 = 0 #pointer1
    p2 = len(ls) - 1 #pointer2
    while p1 != p2:
        if ls[p1] + ls[p2] == n: #if the sum of values at p1 and p2 equals n...
            return True
        elif ls[p1] + ls[p2] < n: #if the sum of values at p1 and p2 is less than n...
            p1 += 1 #increment p1
        elif ls[p1] + ls[p2] > n: #if the sum of values at p1 and p2 is greater than n...
            p2 -= 1 #decrement p2
    return False
"""

# this solution runs in n^2 time
def twoSum(ls, n):
    for p1 in range(len(ls)):
        for p2 in range(p1, p1 + len(ls[p1:])):
            if ls[p1] + ls[p2] == n and p1 != p2:
                return True
    return False

# below is for checking
"""
print(twoSum([1],2)) #False
print(twoSum([-4, 7, -2, 1, 3], -1)) #True
print(twoSum([-4, 7, -2, 1, 3], 6)) #False
print(twoSum([3,1,7,5,0],4)) #True
print(twoSum([2,3,1,7,5,0],4)) #True
"""
