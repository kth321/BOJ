import sys

read = sys.stdin.readline

'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

n, m = map(int, read().split())
parent = [i for i in range(n + 1)]
for _ in range(m):
    op, a, b = map(int, read().split())
    if op == 0:
        union(a, b)
    elif op == 1:
        print('YES' if parent[a] == parent[b] else 'NO')