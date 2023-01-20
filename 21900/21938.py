import sys
from collections import deque

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        if 0 <= x < n and 0 <= y < m * 3 and \
            visited[x][y] == False and sum(graph[x][y:y+3]) / 3 > t:
            visited[x][y] = True
            for d in directions:
                nx, ny = x + d[0], y + d[1] * 3
                q.append((nx, ny))

n, m = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(n)]
visited = [[False] * 3 * m for _ in range(n)]
t = int(read())
res = 0

for i in range(n):
    for j in range(0, m * 3, 3):
        if sum(graph[i][j:j+3]) / 3 >= t and \
            visited[i][j] == False:
            bfs(i, j)
            res += 1
for i in range(n):
    for j in range(0, 3 * m, 3):
        print(visited[i][j], end=' ')
    print()
print()
print(res)