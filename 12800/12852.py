import sys
from collections import deque


def bfs(v):
    q = deque([[v]])
    while q:
        target = q.popleft()
        temp = target[0]
        print(temp)
        if temp == 1:
            return target
        if temp % 3 == 0:
            q.append([temp // 3] + target)
        if temp % 2 == 0:
            q.append([temp // 2] + target)
        q.append([temp - 1] + target)


n = int(sys.stdin.readline())
res = bfs(n)

print(len(res) - 1)
print(res)