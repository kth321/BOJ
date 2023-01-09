from collections import deque
import sys

read = sys.stdin.readline

def bfs(i, j):
    q = deque()
    q.append((i ,j))
    while q:
        x, y = q.popleft()
        if 0 <= x < h and 0 <= y < w and \
            table[x][y] == '1':
            table[x][y] = '0'
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    q.append((x + i, y + j))


while True:
    w, h = map(int, read().split())
    if w == 0 and h == 0:
        break
    table = [list(read().split()) for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if table[i][j] == '1':
                bfs(i, j)
                cnt += 1
    print(cnt)