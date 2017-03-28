# this solution runs in n^3 time
def threeSum(ls, n):
    for p1 in range(len(ls)):
        for p2 in range(p1, p1 + len(ls[p1:])):
            for p3 in range(p2, p2 + len(ls[p2:])):
                if ls[p1] + ls[p2] + ls[p3] == n and p1 != p2 != p3:
                    return True
    return False

# below is for checking
"""
print(threeSum([1,2,3,4,1,2,3],20))
print(threeSum([1,1],2))
"""
