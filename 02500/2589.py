import sys
from collections import deque

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(graph, i, j, n, m):
    q = deque()
    dist = [[-1] * m for _ in range(n)]
    q.append((i, j))
    dist[i][j] = 0
    ret = 0
    
    while q:
        x, y = q.popleft()
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m and\
                dist[nx][ny] == -1 and graph[nx][ny] == 'L':
                dist[nx][ny] = dist[x][y] + 1
                ret = max(ret, dist[nx][ny])
                q.append((nx, ny))
    return ret

def sol():
    n, m = map(int, read().split())
    graph = [list(read().rstrip()) for _ in range(n)]
    visited = set()
    res = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'L' and (i,j) not in visited:
                res = max(res, bfs(graph, i, j, n, m))
                visited.add((j, i))
    return res
print(sol())