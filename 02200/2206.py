import sys
from collections import deque

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

n, m = map(int, read().split())
graph = [list(read().rstrip()) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

q = deque()
q.append((0, 0, 0))

while q:
    x, y, z = q.popleft()
    if x == n - 1 and y == m - 1:
        print(visited[x][y][z])
        exit()
    for d in directions:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < n and 0 <= ny < m and \
            visited[nx][ny][z] == 0:
            if graph[nx][ny] == '0' and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx, ny, z))
            elif graph[nx][ny] == '1' and z == 0:
                visited[nx][ny][z + 1] = visited[x][y][z] + 1
                q.append((nx, ny, z + 1))
print(-1)