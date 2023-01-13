import sys
from collections import deque

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(i, j):
    q = deque()
    cnt = 0

    q.append((i, j))
    while q:
        x, y = q.popleft()
        if 0 <= x < m and 0 <= y < n and \
            table[x][y] == 0:
            table[x][y] = 1
            cnt += 1
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                q.append((nx, ny))
    return cnt
        

m, n, k = map(int, read().split())
table = [[0] * n for _ in range(m)]
res = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, read().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            table[j][i] = 1

for i in range(m):
    for j in range(n):
        if table[i][j] == 0:
            res.append(bfs(i, j))

print(len(res))
print(*sorted(res))