import sys
from collections import deque

read = sys.stdin.readline

directions = (-1, 1)

def bfs(i, j, t):
    q = deque()
    global cnt
    if t == '-':
        q.append(j)
        while q:
            x = q.popleft()
            if 0 <= x < m and visited[i][x] is False and \
                table[i][x] == t:
                visited[i][x] = True
                for d in directions:
                    q.append(x + d)
    else:
        q.append(i)
        while q:
            y = q.popleft()
            if 0 <= y < n and visited[y][j] is False and \
                table[y][j] == t:
                visited[y][j] = True
                for d in directions:
                    q.append(y + d)
    cnt += 1


n, m = map(int, read().split())
table = [list(read().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if visited[i][j] is False:
            bfs(i, j, table[i][j])
print(cnt)