import sys
from collections import deque

read = sys.stdin.readline

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    res = 0
    while q:
        x, y = q.popleft()
        if 0 <= x < n and 0 <= y < m and \
            graph[x][y] == '1':
            graph[x][y] = '0'
            res += 1
            for d in direction:
                q.append((x + d[0], y + d[1]))
    return res

n, m = map(int, read().split())
graph = [read().split() for _ in range(n)]
cnt, res = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '1':
            res = max(res, bfs(i, j))
            cnt += 1
print(cnt, res, sep='\n')