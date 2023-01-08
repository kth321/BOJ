import sys
from collections import deque

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

n, m = map(int, read().split())
maze = [list(read()) for _ in range(n)]
check = [[False] * m for _ in range(n)]
dist = [[0] * m for _ in range(n)]
q = deque()

check[0][0] = True
dist[0][0] = 1
q.append((0, 0))

while q:
    x, y = q.popleft()
    for d in directions:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < n and 0 <= ny < m and \
            check[nx][ny] == False and maze[nx][ny] == '1':
            check[nx][ny] = True
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

print(dist[n-1][m-1])