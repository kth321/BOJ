import sys

read = sys.stdin.readline

n, m = map(int, read().split())
table = set()
res = 0
for _ in range(n):
    table.add(read().rstrip())
for _ in range(m):
    if read().rstrip() in table:
        res += 1
print(res)