import sys
from collections import deque

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def height_reduction(graph, n, m):
    stk = []
    for x in range(n):
        for y in range(m):
            if graph[x][y]:
                tmp = 0
                for d in directions:
                    nx, ny = x + d[0], y + d[1]
                    if 0 <= nx < n and 0 <= ny < m and \
                        not graph[nx][ny]:
                        tmp += 1
                stk.append((x, y, tmp))
    for x, y, val in stk:
        graph[x][y] = max(0, graph[x][y] - val)


def bfs(graph, visited, i, j, n, m):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    ret = 0

    while q:
        x, y = q.popleft()
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and\
                graph[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    

def solution():
    n, m = map(int, read().split())
    graph = [list(map(int, read().split())) for _ in range(n)]
    res = 0

    while True:
        visited = [[False] * m for _ in range(n)]
        tmp = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and graph[i][j]:
                    bfs(graph, visited, i, j, n, m)
                    tmp += 1
            if tmp >= 2:
                return res
        if all(all(line[i] == 0 for i in range(len(line))) for line in graph):
            return 0
        height_reduction(graph, n, m)
        res += 1
        
print(solution())