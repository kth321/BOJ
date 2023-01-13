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
        if 0 <= x < n and 0 <= y < m and \
            table[x][y] == True:
            table[x][y] = False
            cnt += 1
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                q.append((nx, ny))
    return cnt

n, m, k = map(int, read().split())
table = [[False] * m for _ in range(n)]
res = 0

for _ in range(k):
    r, c = map(int, read().split())
    table[r-1][c-1] = True

for i in range(n):
    for j in range(m):
        if table[i][j] == True:
            res = max(res, bfs(i, j))
print(res)