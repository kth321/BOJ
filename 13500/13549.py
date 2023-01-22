import sys
from collections import deque

read = sys.stdin.readline

n, k = map(int, read().split())
dq = deque([n])
visited = [-1 for _ in range(100_001)]
visited[n] = 0

while dq:
    x = dq.popleft()
    if x == k:
        print(visited[x])
        break
    if 0 < 2 * x <= 100_001 and visited[2*x] == -1:
        visited[2*x] = visited[x]
        dq.appendleft(2 * x)
    if 0 <= x - 1 < 100_001 and visited[x-1] == -1:
        visited[x-1] = visited[x] + 1
        dq.append(x - 1)
    if 0 <= x + 1 < 100_001 and visited[x+1] == -1:
        visited[x+1] = visited[x] + 1
        dq.append(x + 1)