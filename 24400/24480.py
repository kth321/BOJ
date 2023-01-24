import sys
from collections import deque

sys.setrecursionlimit(1_000_000)
read = sys.stdin.readline

def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt
    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(graph, i, visited)

n, m, k = map(int, read().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1

for _ in range(m):
    s, e = map(int, read().split())
    graph[s].append(e)
    graph[e].append(s)

for g in graph:
    g.sort(reverse=True)

dfs(graph, k, visited)
for i in range(n + 1):
    if i != 0:
        print(visited[i])