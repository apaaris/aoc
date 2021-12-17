import re
import sys

x1,x2,y1,y2 =  281,311,-74,-54
maxh = y1
count = 0
for vx0 in range(1,x2+1):
    for vy in range(y1,100):
        vx = vx0
        x, y, h = 0, 0, 0
        while x <= x2 and y >= y1:
            x, y = x + vx, y + vy
            h = max(h, y)
            if x1 <= x <= x2 and y1 <= y <= y2:
                maxh = max(h, maxh)
                count += 1
                break
            if vx != 0: vx += -vx/vx
            vy -= 1
print('part 1:', maxh, 'part 2:', count)
