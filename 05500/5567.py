import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
L = [[] for _ in range(n + 1)]
dist = [0] * (n + 1)

for _ in range(int(read())):
    s, e = map(int, read().split())
    L[s].append(e)
    L[e].append(s)
q = deque([1])
cnt = 0

while q:
    x = q.popleft()
    for w in L[x]:
        if w != 1 and dist[w] == 0:
            dist[w] = dist[x] + 1
            q.append(w)
for i in range(n + 1):
    if 0 < dist[i] < 3:
        cnt += 1
print(cnt)