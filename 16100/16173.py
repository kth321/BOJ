import sys
from collections import deque

read = sys.stdin.readline

direction = [(1, 0), (0, 1)]

n = int(read())
graph = [list(map(int, read().split())) 
            for _ in range(n)]
visited = [[False] * n for _ in range(n)]

q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()
    for d in direction:
        nx, ny = x + graph[x][y] * d[0], y + graph[x][y] * d[1]
        if 0 <= nx < n and 0 <= ny < n and \
            visited[nx][ny] == False:
            visited[nx][ny] = True
            q.append((nx, ny))
print('HaruHaru' if visited[-1][-1] else 'Hing')