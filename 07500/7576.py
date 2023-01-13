from collections import deque
import sys

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

m, n = map(int, read().split())
res = 0
table = [list(map(int, read().split()))
        for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if table[i][j] == 1:
            q.append((i, j))

while q:
    x, y = q.popleft()
    for d in directions:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < n and 0 <= ny < m and \
            table[nx][ny] == 0:
            table[nx][ny] = table[x][y] + 1
            q.append((nx, ny))

for line in table:
    if 0 in line:
        print(-1)
        exit()
    res = max(res, max(line))

print(res - 1)