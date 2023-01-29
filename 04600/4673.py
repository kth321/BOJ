res = [True] * 10_001
for i in range(1, 10_001):
    s = str(i)
    tmp = sum(map(int, list(s))) + i
    if tmp <= 10_000:
        res[tmp] = False
for i in range(1, 10_000):
    if res[i] == True:
        print(i)