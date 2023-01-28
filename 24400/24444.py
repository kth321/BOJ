import sys
from collections import deque

read = sys.stdin.readline

n, m, r = map(int, read().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
visited[r] = 1

for _ in range(m):
    s, e = map(int, read().split())
    graph[s].append(e)
    graph[e].append(s)

for g in graph:
    g.sort()

idx = 1
q = deque([r])
while q:
    x = q.popleft()
    for v in graph[x]:
        if visited[v] == 0:
            idx = idx + 1
            visited[v] = idx
            q.append(v)

for i in range(1, n + 1):
    print(visited[i])
