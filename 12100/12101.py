import sys

sys.setrecursionlimit(10 ** 6)

def dfs(res=[]):
    global cnt
    if sum(res) > n:
        return None
    elif sum(res) == n:
        cnt += 1
        if cnt == k:
            print('+'.join(map(str, res)))
            exit()
    for i in range(1, 4):
        dfs(res+[i])

n, k = map(int, input().split())
cnt = 0
dfs()
print(-1)