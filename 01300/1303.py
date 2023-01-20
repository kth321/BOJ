import sys
from collections import deque

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(i, j, c):
    q = deque()
    cnt = 0
    q.append((i, j))
    while q:
        x, y = q.popleft()
        if 0 <= x < m and 0 <= y < n and \
            graph[x][y] == c and visited[x][y] == False:
            cnt += 1
            visited[x][y] = True
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                q.append((nx, ny))
    return cnt

n, m = map(int, read().split())
graph = [list(read().rstrip()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
w, b = 0, 0

for i in range(m):
    for j in range(n):
        if visited[i][j] == False:
            if graph[i][j] == 'W':
                w += bfs(i, j, 'W') ** 2
            else:
                b += bfs(i, j, 'B') ** 2
print(w, b)