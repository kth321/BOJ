import sys

read = sys.stdin.readline

dp = [0] * (100_001)
dp[1] = 1
dp[2] = 2
dp[3] = 2
dp[4] = 3
dp[5] = 3
dp[6] = 6

for i in range(7, 100_001):
    dp[i] = (dp[i-2] + dp[i-4] + dp[i-6]) % 1_000_000_009

for _ in range(int(read())):
    print(dp[int(read())])