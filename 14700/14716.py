import sys
from collections import deque

read = sys.stdin.readline

def bfs(i, j):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0: continue
                nx, ny = x + i, y + j
                if 0 <= nx < m and 0 <= ny < n and \
                    graph[nx][ny] == '1':
                    graph[nx][ny] = '0'
                    q.append((nx, ny))


m, n = map(int, read().split())
graph = [read().split() for _ in range(m)]
res = 0

for i in range(m):
    for j in range(n):
        if graph[i][j] == '1':
            res += 1
            bfs(i, j)
print(res)