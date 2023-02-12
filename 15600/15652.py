def dfs(idx=0, elements=[]):
    if len(elements) == m:
        res.append(elements)
        return None
    for i in range(idx, n):
        dfs(i, elements+[i+1])

n, m = map(int, input().split())
res, output = [], []
dfs()
for r in res:
    print(*r)