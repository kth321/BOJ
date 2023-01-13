import sys
from collections import deque

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(i, j, c):
    q = deque()
    q.append((i, j))
    cnt = 0
    while q:
        x, y = q.popleft()
        if 0 <= x < m and 0 <= y < n and \
            visited[x][y] is False and table[x][y] == c:
            visited[x][y] = True
            cnt += 1
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                q.append((nx, ny))
    return cnt

n, m = map(int, read().split())
table = [list(read().rstrip()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
w, b = 0, 0

for i in range(m):
    for j in range(n):
        print(table[i][j], end=' ')
    print()

for i in range(m):
    for j in range(n):
        if visited[i][j] == False:
            if table[i][j] == 'W':
                w += bfs(i, j, 'W') ** 2
            else:
                b += bfs(i, j, 'B') ** 2
print(w, b)