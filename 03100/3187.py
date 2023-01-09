from collections import deque
import sys

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(i, j):
    q = deque()
    k, v = 0, 0
    q.append((i, j))
    while q:
        x, y = q.popleft()
        if 0 <= x < r and 0 <= y < c and \
            table[x][y] != '#' and visited[x][y] is False:
            visited[x][y] = True
            if table[x][y] == 'k':
                k += 1
            elif table[x][y] == 'v':
                v += 1
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                q.append((nx, ny))
    if k > v:
        return (k, 0)
    else:
        return (0, v)

r, c = map(int, read().split())
table = [list(read().rstrip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
res = [0, 0]

for i in range(r):
    for j in range(c):
        if table[i][j] != '#' and visited[i][j] is False:
            k, v = bfs(i, j)
            res[0] += k
            res[1] += v
print(*res)