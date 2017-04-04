import tkinter
from time import time
from random import shuffle

def plot(xvals, yvals):
    # This is a function for creating a simple scatter plot.  You will use it,
    # but you can ignore the internal workings.
    root = tkinter.Tk()
    c = tkinter.Canvas(root, width=1000, height=800, bg='white') #was 350 x 280
    c.grid()
    #create x-axis
    c.create_line(50,750,950,750, width=3)
    for i in range(0, max(xvals) + 1, 100):
        x = 50 + ((i/100) * 80)
        c.create_text(x,755,anchor='n', text='%s'% (i))
    #y-axis
    c.create_line(50,750,50,50, width=3)
    for i in range(10):
        y = 750 - (i * 75)
        c.create_text(45,y, anchor='e', text='%s'% (.1*i))
    #plot the points
    for i in range(len(xvals)):
        x, y = xvals[i], yvals[i]
        xpixel = int(50 + 700*(x-1))
        ypixel = int(750 - 700*y)
        c.create_oval(xpixel-3,ypixel-3,xpixel+3,ypixel+3, width=1, fill='red')
    root.mainloop()

def rand_list(n):
    ls = [i for i in range(1, n + 1)]
    shuffle(ls)
    return ls

def bubblesort(ls):
    for i in range(len(ls)):
        finished = True
        for k in range(len(ls) - 1 - i):
            if ls[k] > ls[k + 1]:
                finished = False
                ls[k], ls[k + 1] = ls[k + 1], ls[k]
            if finished:
                break
    return ls

def insertionsort(ls):
    for i in range(1, len(ls)):
        tmp = ls[i]
        k = i
        while k > 0 and tmp < ls[k - 1]:
            ls[k] = ls[k - 1]
            k -= 1
        ls[k] = tmp
    return ls

def merge(a, b):
    c = []
    i = j = 0
    while i + j < len(a) + len(b):
        if i >= len(a) or (j < len(b) and b[j] <= a[i]):
            c.append(b[j])
            j += 1
        elif j >= len(b) or a[i] <= b[j]:
            c.append(a[i])
            i += 1
    return c

def mergesort(ls):
    if len(ls) <= 1:
        return ls
    else:
        mid = len(ls) // 2
        return merge(mergesort(ls[:mid]), mergesort(ls[mid:]))

def partition(ls, left, right):
    less = left + 1
    greater = right
    while less <= greater:
        if ls[less] < ls[left]:
            less = less + 1
        else:
            ls[less],ls[greater]= ls[greater],ls[less]
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

# returns the time it takes in seconds for func to sort list of length n
def timing(func, n):
    ls = rand_list(n)
    start = time()
    func(ls)
    end = time()
    return end - start

funcs = [bubblesort, insertionsort, mergesort, quicksort]
xvals = [i for i in range(50, 1001, 50)]
timings = {}

"""
for func in funcs:
    xvals, yvals = [], []
    for n in range(50, 1001, 50):
        values = []
        for i in range(10):
            values.append(timing(quicksort, n))
        mean = sum(values)
        mean /= len(values)
        xvals.append(n)
        yvals.append(mean)
    timings[str(func)[10:-19]] = yvals
    #plot(xvals, yvals)
"""

x = [1,2,3,4,5]
y = [0.1,0.2,0.3,0.4,0.5]
plot(x, y)
