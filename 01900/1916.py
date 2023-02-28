import sys
from heapq import *

read = sys.stdin.readline
INF = int(1e9)

def dijkstra(graph, distance, v):
    q = []
    heappush(q, (0, v))

    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heappush(q, (cost, node[0]))

n, m = int(read()), int(read())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    u, v, w = map(int, read().split())
    graph[u].append((v, w))

a, b = map(int, read().split())
dijkstra(graph, distance, a)
print(distance[b])