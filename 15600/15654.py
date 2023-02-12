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
dfs(sorted(list(map(int, input().split()))))
for r in res:
    print(*r)