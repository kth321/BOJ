import sys

read = sys.stdin.readline

n = int(read())
graph = [list(map(int, read().split())) for _ in range(n)]
while n != 1:
    idx, jdx = 0, 0
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            tmp = []
            for a in range(2):
                for b in range(2):
                    tmp.append(graph[i+a][j+b])
            graph[idx][jdx] = sorted(tmp)[-2]
            jdx += 1
            if jdx >= n//2:
                idx += 1; jdx = 0
    n //= 2
print(graph[0][0])