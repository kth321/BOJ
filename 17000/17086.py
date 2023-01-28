import sys
from collections import deque

read = sys.stdin.readline

n, m = map(int, read().split())
graph = [read().split() for _ in range(n)]
dist = [[0] * m for _ in range(n)]
res = 0

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == '1':
            q.append((i, j))

while q:
    x, y = q.popleft()
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0: continue
            nx, ny = x + i, y + j
            if 0 <= nx < n and 0 <= ny < m and \
                graph[nx][ny] == '0' and dist[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

for l in dist:
    res = max(res, max(l))
print(res)