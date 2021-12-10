from typing import Counter
f = open('in.txt')
ages = f.read().split(',')
f.close()
ages = [int(age) for age in ages]

counter = Counter(ages)
N_days = 256 # (80 for part 1, 256 for part 2)
for day in range(1, N_days+1):
    new_and_reset_fish = counter[0]
    for i in range(8):
        counter[i] = counter[i+1]
    counter[8] = new_and_reset_fish
    counter[6] += new_and_reset_fish
print(sum(counter.values()))
