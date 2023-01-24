from collections import deque
import sys

input = sys.stdin.readline

INF = 1e10
direction = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def bfs():
    dist[0][0] = 0
    queue = deque([(0, 0)])

    while queue:
        print('deque')
        print(*queue)
        print()
        y, x = queue.popleft()

        for i in range(4):
            for d in dist:
                print(*d)
            print()
            dy, dx = direction[i]
            ny, nx = y + dy, x + dx
            if 0 <= ny <= n and 0 <= nx <= m:
                if dist[ny][nx] <= dist[y][x] + graph[y][x][i]:
                    continue
                dist[ny][nx] = dist[y][x] + graph[y][x][i]

                if graph[y][x][i] == 0:
                    # 가중치 변동 없이 이동한 경우 선순위 탐색
                    queue.appendleft((ny, nx))
                else:
                    # 가중치 1을 준 후 이동한 경우 후순위 탐색
                    queue.append((ny, nx))


n, m = map(int, input().split())

graph = [[[1, 1, 1, 1] for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(n): # 3 ~ [0, 1, 2]
    row = input().rstrip()
    for j in range(m): # 5 ~ [0, 1, 2, 3, 4]
        if row[j] == "/":
            graph[i][j + 1][1] = 0
            graph[i + 1][j][2] = 0
        else:
            graph[i][j][0] = 0
            graph[i + 1][j + 1][3] = 0

dist = [[2] * (m + 1) for _ in range(n + 1)]

bfs()
for d in dist:
    print(*d)
print(dist[-1][-1] if dist[-1][-1] != 2 else "NO SOLUTION")