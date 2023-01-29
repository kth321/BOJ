import sys
from heapq import heappop, heappush

read = sys.stdin.readline

n, m = map(int, read().split())
graph = [list(read().rstrip()) for _ in range(n)]
res = []

for i in range(n - 7):
    for j in range(m - 7):
        res1, res2 = 0, 0 # each start is black / white

        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if graph[k][l] == 'B':
                        res1 += 1
                    else:
                        res2 += 1
                else:
                    if graph[k][l] == 'W':
                        res1 += 1
                    else:
                        res2 += 1
        heappush(res, res1)
        heappush(res, res2)
print(heappop(res))