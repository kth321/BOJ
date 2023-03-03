import sys
from collections import deque

read = sys.stdin.readline

def topology(graph, indegree, n):
    res = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        x = q.popleft()
        res.append(x)

        for i in graph[x]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return res

def sol():
    n, m = map(int, read().split())
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, read().split())
        graph[u].append(v)
        indegree[v] += 1
    print(*topology(graph, indegree, n))
sol()