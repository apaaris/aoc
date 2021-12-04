import numpy as np
n, *b = open("in.txt")                  

b = np.loadtxt(b, int).reshape(-1,5,5)
m = np.zeros(b.shape, dtype=bool);

tries = map(int, n.split(','))
lst = []

for n in tries:           
    np.place(m,b == n, True)
    win = (m.all(1) |  m.all(2)).any(1) 
    if win.any():
        lst.append((b * np.invert(m))[win].sum() * n)
        b = b[np.invert(win)]
        m = m[np.invert(win)]

print("Task 1: " + str(lst[0]))
print("Task 2: " + str(lst[len(lst)-1]))
