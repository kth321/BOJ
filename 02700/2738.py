import sys
read = sys.stdin.readline

n, m = map(int, read().split())
A, B = [], []

for i in range(n):
    A.append(list(map(int, read().split())))

for i in range(n):
    B.append(list(map(int, read().split())))

for i in range(n):
    for j in range(m):
        A[i][j] += B[i][j]

for i in A:
    print(*i)