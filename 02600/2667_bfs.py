from collections import deque
import sys

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
res = []

def bfs(i, j):
    q = deque()
    q.append((i, j))
    cnt = 0
    while q:
        x, y = q.popleft()
        if 0 <= x < n and 0 <= y < n and \
            table[x][y] == '1':
            table[x][y] = '0'
            cnt += 1
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                q.append((nx, ny))
    return cnt

n = int(read())
table = [list(read().strip())
            for _ in range(n)]

for i in range(n):
    for j in range(n):
        if table[i][j] == '1':
            res.append(bfs(i, j))
print(len(res))
for r in sorted(res):
    print(r)