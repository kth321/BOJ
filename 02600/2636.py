import sys
from collections import deque

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def remove_cheese(graph, n, m, i=0, j=0):
    q = deque()
    poses = set()
    visited = [[False] * m for _ in range(n)]
    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m and\
                not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny]:
                    poses.add((nx, ny))
                else:
                    q.append((nx, ny))
    for pos in poses:
        x, y = pos
        graph[x][y] = 0
    

def check_size(graph, visited, i, j, n, m):
    q = deque()
    res = 1
    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m and\
                not visited[nx][ny] and graph[nx][ny]:
                visited[nx][ny] = True
                res += 1
                q.append((nx, ny))
    return res

def sol():
    n, m = map(int, read().split())
    graph = [list(map(int, read().split())) for _ in range(n)]
    res = 0
    size = []

    while True:
        visited = [[False] * m for _ in range(n)]
        tmp = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] and not visited[i][j]:
                    tmp += check_size(graph, visited, i, j, n, m)
        size.append(tmp)
        if size[-1] == 0:
            print(res)
            print(size[-2])
            break
        remove_cheese(graph, n, m)
        res += 1
sol()