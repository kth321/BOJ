import sys

read = sys.stdin.readline

dp = [[0] * (15) for _ in range(15)]
dp[0] = [i for i in range(15)]
for i in range(1, 15):
    for j in range(1, 15):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

for _ in range(int(read())):
    k, n = int(read()), int(read())
    print(dp[k][n])