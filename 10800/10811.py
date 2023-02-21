import sys

read = sys.stdin.readline

n, m = map(int, read().split())
nums = [i for i in range(1, n+1)]
for _ in range(m):
    s, e = map(lambda x: x-1, map(int, read().split()))
    nums[s:e+1] = reversed(nums[s:e+1])
print(*nums)