from itertools import combinations_with_replacement

c, up = 1, 2
T = [1]
while c + up <=1000:
    c += up
    T.append(c)
    up += 1

for _ in range(int(input())):
    k = int(input())
    for comb in combinations_with_replacement(T, 3):
        if sum(comb) == k:
            print(1)
            break
    else:
        print(0)