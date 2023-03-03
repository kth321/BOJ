import sys
from collections import deque

read = sys.stdin.readline

def topology(graph, degree, costs, n, w):
    q = deque()
    dp = [0] * (n + 1)
    
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
    return dp[w]

def sol():
    for _ in range(int(read())):
        n, k = map(int, read().split())
        costs = [0] + list(map(int, read().split()))
        graph = [[] for _ in range(n + 1)]
        degree = [0] * (n + 1)

        for _ in range(k):
            u, v = map(int, read().split())
            graph[u].append(v)
            degree[v] += 1
        w = int(read())
        print(topology(graph, degree, costs, n, w))
sol()