#Credits to 4HbQ

import numpy as np
n, *b = open("in.txt")                  

b = np.loadtxt(b, int).reshape(-1,5,5)
m = np.zeros(b.shape, dtype=bool);

tries = map(int, n.split(','))
lst = []

for n in tries:           
    np.place(m,b == n, True)
    win = (m.all(1) |  m.all(2)).any(1) 
    print(win)
    if win.any():
        lst.append((b * ~m)[win].sum() * n)
        b = b[~win]
        m = m[~win]

print("Task 1: " + str(lst[0]))
print("Task 2: " + str(lst[len(lst)-1]))
