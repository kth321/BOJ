def dfs():
    if len(output) == m:
        res.append(output[:])
        return None
    for e in nums:
        output.append(e)
        dfs()
        output.pop()

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
res, output = [], []
dfs()
for r in res:
    print(*r)