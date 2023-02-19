import sys

read = sys.stdin.readline

def sol(i, j, n):
    if n == 1:
        if graph[i][j] == 0:
            global w
            w += 1
        else:
            global b
            b += 1
        return None
    if all(graph[a][b] for a in range(i, i+n)
                        for b in range(j, j+n)):
        b += 1
        return None
    if all(graph[a][b] == 0 for a in range(i, i+n)
                        for b in range(j, j+n)):
        w += 1
        return None
    sol(i, j, n // 2)
    sol(i + n//2, j, n // 2)
    sol(i, j + n//2, n // 2)
    sol(i + n//2, j + n//2, n // 2)

n = int(read())
graph = [list(map(int, read().split())) for _ in range(n)]
w, b = 0, 0
sol(0, 0, n)
print(w); print(b)