import sys
from collections import deque

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(i=0, j=0):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m and \
                dist[nx][ny] == 0 and graph[nx][ny] == '1':
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))


n, m = map(int, read().split())
graph = [list(read().rstrip()) for _ in range(n)]
dist = [[0] * m for _ in range(n)]
dist[0][0] = 1
bfs()
print(dist[n-1][m-1])