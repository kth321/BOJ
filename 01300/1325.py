import sys
from collections import deque

read = sys.stdin.readline
def MIS(): return map(int, read().split())


n, m = MIS()
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    e, s = MIS()
    graph[s].append(e)

max_depth = 0
res = [0] * (n + 1)

for i in range(1, n + 1):
    q = deque([i])
    visited = [False] * (n + 1)
    cnt = 0
    while q:
        x = q.popleft()
        if visited[x] == False:
            visited[x] = True
            cnt += 1
            for v in graph[x]:
                q.append(v)
    res[i] = cnt
print(*[i for i in range(n + 1)
        if res[i] == max(res)])