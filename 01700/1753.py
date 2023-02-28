import sys
from heapq import *

read = sys.stdin.readline
INF = int(1e9)

def dijkstra(v):
    q = []
    heappush(q, (0, v))
    distance[v] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heappush(q, (cost, node[0]))

v, e = map(int, read().split())
start_v = int(read())

graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    u, v, w = map(int, read().split())
    graph[u].append((v, w))

dijkstra(start_v)

for dist in distance[1:]:
    print(dist if dist != INF else 'INF')