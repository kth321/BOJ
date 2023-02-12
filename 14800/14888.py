import sys

input = sys.stdin.readline
v = 1e9

def dfs(idx, res, plus, minus, mul, div):
    global max_v, min_v
    if idx == n:
        max_v = max(res, max_v)
        min_v = min(res, min_v)
        return None

    if plus:
        dfs(idx+1, res + nums[idx], plus-1, minus, mul, div)
    if minus:
        dfs(idx+1, res - nums[idx], plus, minus-1, mul, div)
    if mul:
        dfs(idx+1, res * nums[idx], plus, minus, mul-1, div)
    if div:
        dfs(idx+1, int(res / nums[idx]), plus, minus, mul, div-1)

n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))
max_v, min_v = -v, v
dfs(1, nums[0], op[0], op[1], op[2], op[3])
print(max_v)
print(min_v)