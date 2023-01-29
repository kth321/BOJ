import sys
from collections import deque

read = sys.stdin.readline

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(i, j, c):
    q = deque()
    q.append((i, j))
    visited[i]
    while q:
        x, y = q.popleft()
        if 0 <= x < n and 0 <= y < n and \
            not visited[x][y] and graph[x][y] == c:
            visited[x][y] = True
            for d in direction:
                q.append((x + d[0], y + d[1]))

n = int(read())
graph = [list(read().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
c1, c2 = 0, 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, graph[i][j])
            c1 += 1

for line in graph:
    for i in range(n):
        if line[i] == 'G':
            line[i] = 'R'
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, graph[i][j])
            c2 += 1
print(c1, c2)