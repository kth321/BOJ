import sys

read = sys.stdin.readline

def dfs(nodes, n, v):
    nodes[v] = -2
    for i in range(n):
        if v == nodes[i]:
            dfs(nodes, n, i)


def sol():
    n = int(read())
    nodes = list(map(int, read().split()))
    ban = int(read())
    res = 0

    dfs(nodes, n, ban)
    for i in range(n):
        if nodes[i] != -2 and i not in nodes:
            res += 1
    return res
print(sol())