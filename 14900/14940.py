import sys
from collections import deque

read = sys.stdin.readline

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

n, m = map(int, read().split())
graph = [read().split() for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == '0':
            dist[i][j] = 0
        elif graph[i][j] == '2':
            dist[i][j] = 0
            q.append((i, j))
while q:
    x, y = q.popleft()
    for d in direction:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < n and 0 <= ny < m and \
            graph[nx][ny] == '1' and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
for line in dist:
    print(*line)