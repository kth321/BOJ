from collections import deque
import sys

read = sys.stdin.readline

def bfs(start_v):
    q = deque([start_v])
    dist = [0] * n
    visited = []
    while q:
        x = q.popleft()
        if x not in visited:
            visited.append(x)
        for friend in friends[x]:
            if friend not in visited and dist[friend-1] == 0:
                dist[friend-1] = dist[x-1] + 1
                q.append(friend)
    return sum(dist)


n, m = map(int, read().split())
friends = {i + 1: []  for i in range(n)}
res = []

for _ in range(m):
    s, e = map(int, read().split())
    friends[s].append(e)
    friends[e].append(s)

for i in range(1, n + 1):
    res.append(bfs(i))
print(res.index(min(res)) + 1)