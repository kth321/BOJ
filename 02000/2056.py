import sys
from collections import deque

read = sys.stdin.readline

def topology(graph, costs, degree, dp, n):
    q = deque()
    for i in range(1, n + 1):
        if degree[i] == 0:
            q.append(i)
            dp[i] = costs[i]
    while q:
        x = q.popleft()
        for i in graph[x]:
            degree[i] -= 1
            dp[i] = max(dp[i], dp[x] + costs[i])
            if degree[i] == 0:
                q.append(i)
    return max(dp)

def sol():
    n = int(read())
    graph = [[] for _ in range(n + 1)]
    costs = [0] * (n + 1)
    degree = [0] * (n + 1)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        cost, d, *pres = map(int, read().split())
        costs[i] = cost
        degree[i] = d
        for pre in pres:
            graph[pre].append(i)
    print(topology(graph, costs, degree, dp, n))

sol()