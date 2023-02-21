import sys
from collections import deque

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(i, j, shark_size):
    q = deque()
    visited = [[False] * n for _ in range(n)]
    ret = []

    q.append((0, i, j))

    while q:
        dist, x, y = q.popleft()
        visited[x][y] = True
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < n and \
                not visited[nx][ny]:
                if 1 <= graph[nx][ny] <= 6 and \
                    graph[nx][ny] < shark_size:
                    q.append((dist+1, nx, ny))
                    ret.append((dist+1, nx, ny))
                elif graph[nx][ny] == 0 or \
                    graph[nx][ny] == shark_size:
                    q.append((dist+1, nx, ny))
    return sorted(ret)[0] if ret else False

def find_fish():
    for i in range(n):
        for j in range(n):
            if 1 <= graph[i][j] <= 6:
                return True
    return False

n = int(read())
graph = [list(map(int, read().split())) for _ in range(n)]
if find_fish():
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                graph[i][j] = 0
                x, y = i, j

    res, eat, shark_size = 0, 0, 2
    while True:
        ret = bfs(x, y, shark_size)
        if ret:
            dist, nx, ny = ret
            res += dist
            graph[nx][ny] = 0
            eat += 1
            if eat >= shark_size:
                shark_size += 1
                eat = 0
            x, y = nx ,ny
        else:
            break
    print(res)
else:
    print(0)