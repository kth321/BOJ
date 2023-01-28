import sys
from collections import deque

read = sys.stdin.readline

direction = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1),
                (1, -2), (-1, -2), (-2, -1)]

for _ in range(int(read())):
    n = int(read())
    r1, c1 = map(int, read().split())
    r2, c2 = map(int, read().split())
    dist = [[-1] * n for _ in range(n)]
    dist[r1][c1] = 0
    q = deque()
    q.append((r1, c1))

    while q:
        x, y = q.popleft()
        if x == r2 and y == c2:
            print(dist[x][y])
            break
        for d in direction:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < n and\
                dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))