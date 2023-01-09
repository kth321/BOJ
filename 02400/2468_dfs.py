import sys

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def dfs(i, j, h):
    stk = []
    stk.append((i, j))
    while stk:
        x, y = stk.pop()
        if 0 <= x < n and 0 <= y < n and \
            table[x][y] > h and visited[x][y] is False:
            visited[x][y] = True
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                stk.append((nx, ny))

n = int(read())
res = 0
table = [list(map(int, read().split()))
            for _ in range(n)]

for k in range(100):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if table[i][j] > k and visited[i][j] is False:
                dfs(i, j, k)
                cnt += 1
    res = max(res, cnt)
print(res)