
lines = [line.strip().split(' ') for line in open("in.txt")]
lines = [(line[0], [line.split('=')[1] for line in line[1].split(',')]) for line in lines]
lines = [(*[tuple([*map(int,line.split('..'))]) for line in line[1]], line[0] == "on") for line in lines]

def countCubes(c):
  if c[0][0] > c[0][1] or c[1][0] > c[1][1] or c[2][0] > c[2][1]: return 0
  return (c[0][1]-c[0][0]+1) * (c[1][1]-c[1][0]+1) * (c[2][1]-c[2][0]+1)

def intersect(a, b):
  return tuple((max(a[x][0], b[x][0]), min(a[x][1], b[x][1])) for x in range(3))

def intersects(a, b):
  return countCubes(intersect(a,b)) != 0

cuboids = []; fivties = ((-50, 50), (-50, 50), (-50, 50))

for line in lines:
  intersections = [*[tuple([*intersect(cuboid, line), not cuboid[3]]) for cuboid in cuboids if intersects(line, cuboid)]]
  cuboids.extend([line, *intersections] if line[3] else intersections)

print(*(sum(countCubes(transform(cuboid)) * [-1,1][cuboid[3]] for cuboid in cuboids) for transform in [lambda x:intersect(x, fivties), lambda x:x]))
