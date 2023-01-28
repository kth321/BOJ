import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))
dist = [-1] * n
dist[0] = 0
q = deque([0])

while q:
    idx = q.popleft()
    if nums[idx] != 0:
        for i in range(1, nums[idx] + 1):
            if idx + i < n and dist[idx + i] == -1:
                dist[idx + i] = dist[idx] + 1
                q.append(idx + i)
print(dist[-1])