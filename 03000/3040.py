from itertools import combinations

dwarf = [int(input()) for _ in range(9)]
for comb in combinations(dwarf, 7):
    if sum(comb) == 100:
        for i in comb:
            print(i)