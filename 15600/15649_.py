def dfs(elements):
    if len(output) == m:
        res.append(output[:])
        return None
    for e in elements:
        next = elements[:]
        next.remove(e)
        output.append(e)
        dfs(next)
        output.remove(e)

n, m = map(int, input().split())
res, output = [], []
dfs(list(range(1, n + 1)))
for r in res:
    print(*r)