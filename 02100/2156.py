import sys

read = sys.stdin.readline

n = int(read())
nums = [0] * 10_001
dp = [0] * 10_001
for i in range(n):
    nums[i+1] = int(read())

dp[1], dp[2] = nums[1], nums[1] + nums[2]
for i in range(3, n+1):
    dp[i] = max(dp[i-1], nums[i] + nums[i-1] + dp[i-3], nums[i] + dp[i-2])
print(max(dp))