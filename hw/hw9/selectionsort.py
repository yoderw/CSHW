# disregarding the running time of range(), len(), min() and index(),
# the running time of selection sort is: n

def selectionsort(aList):
    ls = aList
    for i in range(len(ls)):
        i_value = ls[i]
        min_value = min(ls[i:])
        min_index = ls[i:].index(min_value) + i
        ls[i] = min_value
        ls[min_index] = i_value

"""
x = [4,2,3,1,1]
y = x.copy()
y.sort()
selectionsort(x)

x = list("7189237589012735891723408912308768910635192730478129320561091923857123905")
for i in range(len(x)):
    x[i] = int(x[i])
y = x.copy()
y.sort()
selectionsort(x)

print(x == y)
"""
