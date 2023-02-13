# def dfs(idx, res, plus, minus, mul, div):
#     global max_v, min_v
#     if idx == n:
#         max_v = max(max_v, eval(res))
#         min_v = min(min_v, eval(res))
#         return None
#     if plus:
#         dfs(idx+1, res + '+' + nums[idx], plus-1, minus, mul, div)
#     if minus:
#         dfs(idx+1, res + '-' + nums[idx], plus, minus-1, mul, div)
#     if mul:
#         dfs(idx+1, res + '*' + nums[idx], plus, minus, mul-1, div)
#     if div:
#         dfs(idx+1, res + '//' + nums[idx], plus, minus, mul, div-1)

# n = int(input())
# nums = input().split()
# plus, minus, mul, div = map(int, input().split())
# v = 1e9
# max_v, min_v = -v, v
# dfs(1, nums[0], plus, minus, mul, div)
# print(max_v)
# print(min_v)

def dfs(p, m, mul, div, op, idx, pre, now):
    if idx == n:
        global max_v, min_v
        now = operate(op, pre, now)
        max_v = max(max_v, now)
        min_v = min(min_v, now)
        return None
    
    if p:
        dfs(p-1, m, mul, div, 1, idx+1, operate(op, pre, now), nums[idx])
    if m:
        dfs(p, m-1, mul, div, 2, idx+1, operate(op, pre, now), nums[idx])
    if op == 0:
        if mul:
            dfs(p, m, mul-1, div, 0, idx+1, pre * nums[idx], 0)
        if div:
            dfs(p, m, mul, div-1, 0, idx+1, divide(pre, nums[idx]), 0)
    else:
        if mul:
            dfs(p, m, mul-1, div, op, idx+1, pre, now * nums[idx])
        if div:
            dfs(p, m, mul, div-1, op, idx+1, pre, divide(pre, nums[idx]))

def operate(op, num1, num2):
    if op == 0:
        return num1
    elif op == 1:
        return num1 + num2
    else:
        return num1 - num2

def divide(num1, num2):
    return num1 // num2 if num2 != 0 else None

n = int(input())
nums = list(map(int, input().split()))
p, m, mul, div = map(int, input().split())
v = 1e9
max_v, min_v = -v, v

dfs(p, m, mul, div, 0, 1, nums[0], nums[1])
print(max_v)
print(min_v)