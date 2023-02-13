import sys

read = sys.stdin.readline
mod_v = 1_000_000_009

dp = [[0, 0, 0] for _ in range(100_001)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 100_001):
        dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % mod_v
        dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % mod_v
        dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % mod_v

for _ in range(int(read())):
    n = int(input())
    print(sum(dp[n]) % mod_v)