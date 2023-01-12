import sys

read = sys.stdin.readline

n, m = map(int, read().split())
a = sorted(list(map(int, read().split())),
            reverse=True)
b = sorted(list(map(int, read().split())))
a_i, b_i = 0, 0
res = 0

while a_i < n and b_i < m:
    if a[a_i] <= b[b_i]:
        break
    if a[a_i] > b[b_i]:
        res += a[a_i] - b[b_i]
        a_i += 1
        b_i += 1
print(res)