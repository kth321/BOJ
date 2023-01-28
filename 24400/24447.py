import sys
from collections import deque

read = sys.stdin.readline

n, m, r = map(int, read().split())
graph = [[] for _ in range(n + 1)]
t = [0] * (n + 1)
d = [-1] * (n + 1)
d[r], t[r] = 0, 1
res = 0

for _ in range(m):
    s, e = map(int, read().split())
    graph[s].append(e)
    graph[e].append(s)

q = deque([r])
idx = 1

while q:
    v = q.popleft()
    for w in graph[v]:
        if d[w] == -1:
            idx += 1
            t[w] = idx
            d[w] = d[v] + 1
            q.append(w)

for i, j in zip(t, d):
    res += i * j
print(res)