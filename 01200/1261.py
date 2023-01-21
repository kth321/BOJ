import sys
from collections import deque

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs():
    dq = deque()
    dq.append((0, 0))
    res = 0
    while dq:
        x, y = dq.popleft()
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m and \
                dist[nx][ny] == -1:
                if graph[nx][ny] == '0':
                    dq.appendleft((nx, ny))
                    dist[nx][ny] = dist[x][y]
                else:
                    dq.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1


m, n = map(int, read().split())
graph = [list(read().rstrip()) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
dist[0][0] = 0
bfs()
print(dist[n-1][m-1])