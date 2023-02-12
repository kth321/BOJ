def dfs(elements=[]):
    if len(elements) == m:
        print(*elements)
        return None
    for i in range(n):
        dfs(elements+[nums[i]])

n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
n = len(nums)
dfs()