import sys
from collections import deque

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(i, j):
    q = deque()
    ret = []
    q.append((i, j))
    ret.append((i, j))

    while q:
        x, y = q.popleft()
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < n and\
                not visited[nx][ny] and\
                l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                visited[nx][ny] = True
                q.append((nx, ny))
                ret.append((nx, ny))
    return ret


n, l, r = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(n)]
res = 0

while True:
    visited = [[False] * n for _ in range(n)]
    change = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                ret = bfs(i, j)
                if len(ret) > 1:
                    change = True
                    elem = sum(graph[x][y] for x, y in ret) // len(ret)
                    for x, y in ret:
                        graph[x][y] = elem
    if not change:
        break
    res += 1
print(res)