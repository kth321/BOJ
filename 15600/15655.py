def dfs(idx=0, elements=[]):
    print(elements)
    if len(elements) == m:
        res.append(elements)
        return None
    for i in range(idx, n):
        dfs(i+1, elements+[nums[i]])

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
res = []
dfs()
for r in res:
    print(*r)