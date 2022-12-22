import sys

read = sys.stdin.readline

n = int(read())
nums = sorted([int(read()) for _ in range(n)])
res = 0

for i in range(n):
    res = max(res, nums[i] * (n - i))
print(res)