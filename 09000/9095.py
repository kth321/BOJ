import sys

read = sys.stdin.readline

dp = [0, 1, 2, 4] + [0] * 7

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(int(read())):
    print(dp[int(read())])