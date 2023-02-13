import sys

read = sys.stdin.readline

dp = [[1, 0, 0] for _ in range(10_001)]
dp[1][0] = 1
dp[2][0] = 1
dp[2][1] = 1
dp[3][0] = 1
dp[3][1] = 1
dp[3][2] = 1

for i in range(4, 10_001):
    dp[i][1] = sum(dp[i-2][:2])
    dp[i][2] = sum(dp[i-3])

for _ in range(int(read())):
    n = int(input())
    print(sum(dp[n]))