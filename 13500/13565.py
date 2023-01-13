import sys

sys.setrecursionlimit(1_000_000)
read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def dfs(i, j, visited):
    visited[i][j] = True
    for d in directions:
        nx, ny = i + d[0], j + d[1]
        if 0 <= nx < m and 0 <= ny < n and \
            visited[nx][ny] == False and table[nx][ny] == '0':
            dfs(nx, ny, visited)

m, n = map(int, read().split())
table = [list(read().rstrip()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
res = 'NO'

for i in range(n):
    if table[0][i] == '0':
        dfs(0, i, visited)

for i in range(n):
    if visited[m-1][i] == True:
        res = 'YES'
print(res)