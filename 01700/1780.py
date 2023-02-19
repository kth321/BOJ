import sys

read = sys.stdin.readline

def sol(i, j, n):
    if n == 1:
        res[graph[i][j]] += 1
        return
    
    for k in range(-1, 2):
        if all(graph[a][b] == k for a in range(i, i + n)
                                for b in range(j, j + n)):
            res[k] += 1
            return None
        
    for a in range(0, n, n//3):
        for b in range(0, n, n//3):
            sol(i + a, j + b, n//3)


n = int(read())
graph = [list(map(int, read().split())) for _ in range(n)]
res = [0, 0, 0]
sol(0, 0, n)

for i in range(-1, 2):
    print(res[i])