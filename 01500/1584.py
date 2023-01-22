import sys
from collections import deque

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


graph = [[0] * 501 for _ in range(501)] # 1 위험, 2 죽음
dist = [[-1] * 501 for _ in range(501)]
dist[0][0] = 0

for _ in range(int(read())):
    x1, y1, x2, y2 = map(int, read().split())
    if x1 > x2: x2, x1 = x1, x2
    if y1 > y2: y2, y1 = y1, y2
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            graph[i][j] = 1

for _ in range(int(read())):
    x1, y1, x2, y2 = map(int, read().split())
    if x1 > x2: x2, x1 = x1, x2
    if y1 > y2: y2, y1 = y1, y2
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            graph[i][j] = 2

dq = deque()
dq.append((0, 0))
while dq:
    x, y = dq.popleft()
    for d in directions:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx <= 500 and 0 <= ny <= 500 and \
            dist[nx][ny] == -1 and graph[nx][ny] < 2:
            if graph[nx][ny] == 0:
                dq.appendleft((nx, ny))
                dist[nx][ny] = dist[x][y]
            else:
                dq.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1

print(-1 if dist[-1][-1] == -1 else dist[-1][-1])