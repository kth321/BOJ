import sys
from collections import deque

read = sys.stdin.readline

n, m, k, x = map(int, read().split())
graph = [[] for _ in range(n + 1)]
dist = [-1] * (n + 1)

for _ in range(m):
    s, e = map(int, read().split())
    graph[s].append(e)

q = deque([x])
dist[x] = 0

while q:
    y = q.popleft()
    for node in graph[y]:
        if dist[node] == -1:
            dist[node] = dist[y] + 1
            q.append(node)
if k in dist:
    for i in range(1, n + 1):
        if dist[i] == k:
            print(i)
else:
    print(-1)