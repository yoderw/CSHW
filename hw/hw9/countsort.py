counts = lambda xs: [xs.count(i) for i in range(max(xs) + 1)]

def counts(xs, n):
	ls = [0 for i in range(n)]
	for i in xs:
		ls[i] += 1
	return ls

def countsort(aList, m):
    ls = counts(aList, m)
    xs = [i for i in range(len(ls)) for j in range(ls[i])]
    for i in range(len(xs)):
        aList[i] = xs[i]

"""
x = [4,2,3,1,1]
y = x.copy()
y.sort()
countsort(x, 5)

x = list("7189237589012735891723408912308768910635192730478129320561091923857123905")
for i in range(len(x)):
    x[i] = int(x[i])
y = x.copy()
y.sort()
countsort(x, 10)

print(x == y)
"""
