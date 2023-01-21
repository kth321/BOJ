import sys
import heapq

read = sys.stdin.readline

def prim(x):
    visited[x] = True
    heap = graph[x]
    heapq.heapify(heap)
    res = 0

    while heap:
        weight, w = heapq.heappop(heap)
        if visited[w] == False:
            visited[w] = True
            res += weight
            for edge in graph[w]:
                if visited[edge[1]] == False:
                    heapq.heappush(heap, edge)
    return res

n, m = int(read()), int(read())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v, weight = map(int, read().split())
    graph[u].append((weight, v))
    graph[v].append((weight, u))

print(prim(1))