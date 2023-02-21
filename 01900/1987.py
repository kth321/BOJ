import sys

read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def dfs(x=0, y=0, cnt=1):
    global res
    res = max(res, cnt)
    for d in directions:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < r and 0 <= ny < c and\
            not visited[graph[nx][ny]]:
            visited[graph[nx][ny]] = 1
            dfs(nx, ny, cnt+1)
            visited[graph[nx][ny]] = 0

r, c = map(int, read().split())
graph = [list(map(lambda x: ord(x) - 65, read().rstrip()))
            for _ in range(r)]
visited = [0] * 26
visited[graph[0][0]] = 1
res = 1
dfs()
print(res)