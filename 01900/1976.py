import sys

sys.setrecursionlimit(10 ** 6)
read = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = int(read()), int(read())
parent = [i for i in range(n + 1)]

for i in range(1, m + 1):
    connection = list(map(int, read().split()))
    for j in range(1, n + 1):
        if connection[j - 1] == 1:
            union(i, j)
plan = list(map(int, read().split()))
first = parent[plan[0]]
print('YES' if all(first == parent[i] for i in plan) else 'NO')