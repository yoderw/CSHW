def partition(ls, left, right): 
	less = left + 1
	greater = right
	while less <= greater:
		if ls[less] < ls[left]: 
			less = less + 1
		else:
			ls[less], ls[greater] = ls[greater], ls[less] 
			greater = greater - 1
	ls[left], ls[less - 1] = ls[less - 1], ls[left] 
	return less - 1

def qshelp(ls, first, last): 
	if first < last:
		pivot = partition(ls, first, last)
		qshelp(ls, first, pivot-1)
		qshelp(ls, pivot+1, last)

def quicksort(ls): 
	qshelp(ls, 0, len(ls)-1)

xs = [4,2,3,1,1]
quicksort(xs)
print(xs)