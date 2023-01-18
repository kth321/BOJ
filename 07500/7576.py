import sys
from collections import deque

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs():
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((i, j))
    
    while q:
        x, y = q.popleft()
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m and \
                graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))


m, n = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(n)]
res = 0
bfs()
for line in graph:
    if 0 in line:
        print(-1)
        exit()
    res = max(res, max(line))
print(res - 1)