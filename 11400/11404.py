import sys

read = sys.stdin.readline
INF = int(1e5)

n, m = int(read()), int(read())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    u, v, w = map(int, read().split())
    graph[u][v] = min(graph[u][v], w)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for line in graph[1:]:
    print(*line[1:])