from collections import deque
import sys

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        if 0 <= x < n and 0 <= y < m and \
            table[x][y] == 1:
            table[x][y] = 0
            for d in directions:
                q.append((x + d[0], y + d[1]))

for T in range(int(read())):
    m, n, k = map(int, read().split())
    table = [[0] * m for _ in range(n)]
    res = 0

    for _ in range(k):
        i, j = map(int, read().split())
        table[j][i] = 1

    for i in range(n):
        for j in range(m):
            if table[i][j] == 1:
                bfs(i, j)
                res += 1
    print(res)