import sys
import heapq

input = sys.stdin.readline
def MIIS(): return map(int, input().split())

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
    

v, e = MIIS()
graph = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)

for _ in range(e):
    u, v, weight = MIIS()
    graph[u].append([weight, v])
    graph[v].append([weight, u])

print(prim(1))