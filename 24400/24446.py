import sys
from collections import deque

read = sys.stdin.readline

n, m, r = map(int, read().split())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
visited[r] = 0

for _ in range(m):
    s, e = map(int, read().split())
    graph[s].append(e)
    graph[e].append(s)

q = deque([r])
while q:
    v = q.popleft()
    for w in graph[v]:
        if visited[w] == -1:
            visited[w] = visited[v] + 1
            q.append(w)

for i in range(1, n + 1):
    print(visited[i])