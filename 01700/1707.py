import sys

read = sys.stdin.readline

def dfs(visited, graph, x):
    stk = []
    stk.append(x)
    visited[x] = 1

    while stk:
        v = stk.pop()
        for w in graph[v]:
            if visited[w] == 0:
                stk.append(w)
                if visited[v] == 1:
                    visited[w] = -1
                else:
                    visited[w] = 1
            elif visited[v] == visited[w]:
                return False
    return True

for _ in range(int(read())):
    v, e = map(int, read().split())
    graph = [set() for _ in range(v + 1)]
    visited = [0] * (len(graph) + 1)

    for _ in range(e):
        st, en = map(int, read().split())
        graph[st].add(en)
        graph[en].add(st)
    
    for w in range(v+1):
        if not visited[w]:
            if not dfs(visited, graph, w):
                print('NO')
                break
    else:
        print('YES')