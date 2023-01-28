import sys
from collections import deque

read = sys.stdin.readline

n, m = map(int, read().split())
graph = [[] for _ in range(n + 1)]
dist = [0] * (n + 1)
dist[1] = 1
for _ in range(m):
    s, e = map(int, read().split())
    graph[s].append(e)
    graph[e].append(s)

q = deque([1])
while q:
    v = q.popleft()
    for w in graph[v]:
        if dist[w] == 0:
            dist[w] = dist[v] + 1
            q.append(w)

max_d = max(dist)
print(dist.index(max_d), max_d - 1, end=' ')
print(len([i for i in dist if i == max_d]))