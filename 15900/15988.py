import sys

read = sys.stdin.readline

dp = [0, 1, 2, 4] + [0] * 999_997

for i in range(4, 1_000_001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1_000_000_009

for _ in range(int(read())):
    print(dp[int(read())])