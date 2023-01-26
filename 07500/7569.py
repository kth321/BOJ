import sys
from collections import deque

read = sys.stdin.readline

direction = [(-1, 0, 0), (0, -1, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)]

def bfs():
    q = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    q.append((i, j, k))
    while q:
        x, y, z = q.popleft()
        for d in direction:
            nx, ny, nz = x + d[0], y + d[1], z + d[2]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and\
                graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = graph[x][y][z] + 1
                q.append((nx, ny, nz))
                

m, n, h = map(int, read().split()) # 5 3 2
graph = [[list(map(int ,read().split())) for _ in range(n)]
                for _ in range(h)]
res = 0
bfs()
for layer in graph:
    for line in layer:
        print(*line)
    print()
for i in range(h):
    for line in graph[i]:
        if 0 in line:
            print(-1)
            exit()
        res = max(res, max(line))
print(res - 1)