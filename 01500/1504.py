import sys
from heapq import *

read = sys.stdin.readline
INF = int(1e9)

def get_short_path(graph, n, v1, v2):
    res1 = dijkstra(graph, n, 1, v1) + dijkstra(graph, n, v1, v2) +\
          dijkstra(graph, n, v2, n)
    res2 = dijkstra(graph, n, 1, v2) + dijkstra(graph, n, v2, v1) +\
          dijkstra(graph, n, v1, n)
    res = min(res1, res2)

    return res if res < INF else -1

def dijkstra(graph, n, start, end):
    distance = [INF] * (n + 1)
    q = []

    distance[start] = 0
    heappush(q, (0, start))

    while q:
        dist, now = heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))
    return distance[end]

def sol():
    n, e = map(int, read().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(e):
        s, e, w = map(int, read().split())
        graph[s].append((e, w))
        graph[e].append((s, w))
    v1, v2 = map(int, read().split())

    print(get_short_path(graph, n, v1, v2))
sol()