import sys
from collections import deque

read = sys.stdin.readline

direction = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

n = int(read())
r1, c1, r2, c2 = map(int, read().split())
graph = [[0] * n for _ in range(n)]
q = deque()
q.append((r1, c1))

while q:
    x, y = q.popleft()
    if x == r2 and y == c2:
        print(graph[x][y])
        break
    for d in direction:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < n and 0 <= ny < n and\
            graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))
else:
    print(-1)