import sys
from copy import deepcopy
from collections import deque

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs():
    global res

    tmp = deepcopy(table)
    q = deque()
    cnt = 0

    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m and \
                tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                q.append((nx, ny))
    
    for line in tmp:
        cnt += line.count(0)
    res = max(res, cnt)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if table[i][j] == 0:
                table[i][j] = 1
                wall(cnt + 1)
                table[i][j] = 0

n, m = map(int, read().split())
table = [list(map(int, read().split())) for _ in range(n)]
res = 0

wall(0)
print(res)