def dfs(idx=0, elements=[]):
    if len(elements) == m:
        print(*elements)
        return None
    for i in range(idx, len(nums)):
        dfs(i, elements+[nums[i]])

n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
dfs()