import sys

read = sys.stdin.readline

dp = [[0, 0] for _ in range(100001)]
dp[1] = [1, 0]
dp[2] = [1, 1]
dp[3] = [2, 2]

for i in range(4, 100001):
    dp[i][0] = dp[i-1][1] + dp[i-2][1] + dp[i-3][1]
    dp[i][1] = dp[i-1][0] + dp[i-2][0] + dp[i-3][0]

for _ in range(int(read())):
    print(*dp[int(input())])