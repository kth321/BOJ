import sys

read = sys.stdin.readline

for T in range(int(read())):
    n, stocks = int(read()), list(map(int, read().split()))
    max_v = stocks[-1]
    res = 0

    for i in range(n - 2, -1, -1):
        if stocks[i] < max_v:
            res += max_v - stocks[i]
        else:
            max_v = stocks[i]
    print(res)