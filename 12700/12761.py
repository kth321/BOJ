import sys
from collections import deque

read = sys.stdin.readline

a, b, n, m = map(int, read().split())
S = 10 ** 5 + 1
graph = [0] * S
q = deque([n])
while q:
    if graph[m] != 0:
        print(graph[m])
        break

    v = q.popleft()
    if v - 1 >= 0 and graph[v - 1] == 0:
        graph[v - 1] = graph[v] + 1
        q.append(v - 1)

    if v + 1 < S and graph[v + 1] == 0:
        graph[v + 1] = graph[v] + 1
        q.append(v - 1)

    if v + a < S and graph[v + a] == 0:
        graph[v + a] = graph[v] + 1
        q.append(v + a)

    if v + b < S and graph[v + b] == 0:
        graph[v + b] = graph[v] + 1
        q.append(v + b)

    if v - a >= 0 and graph[v - a] == 0:
        graph[v -a] = graph[v] + 1
        q.append(v - a)

    if v - b >= 0 and graph[v - b] == 0:
        graph[v - b] = graph[v] + 1
        q.append(v - b)

    if 0 <= a * v < S and graph[a * v] == 0:
        graph[a * v] = graph[v] + 1
        q.append(a * v)

    if 0 <= b * v < S and graph[b * v ] == 0:
        graph[b * v] = graph[v] + 1
        q.append(b * v)