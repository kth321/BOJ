def dfs(idx, res, plus, minus, mul, div):
    global max_v, min_v
    if idx == n:
        max_v = max(max_v, eval(res))
        min_v = min(min_v, eval(res))
        return None
    if plus:
        dfs(idx+1, res + '+' + nums[idx], plus-1, minus, mul, div)
    if minus:
        dfs(idx+1, res + '-' + nums[idx], plus, minus-1, mul, div)
    if mul:
        dfs(idx+1, res + '*' + nums[idx], plus, minus, mul-1, div)
    if div:
        dfs(idx+1, res + '//' + nums[idx], plus, minus, mul, div-1)

n = int(input())
nums = input().split()
plus, minus, mul, div = map(int, input().split())
v = 1e9
max_v, min_v = -v, v
dfs(1, nums[0], plus, minus, mul, div)
print(max_v)
print(min_v)