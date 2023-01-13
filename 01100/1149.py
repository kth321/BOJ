import sys

read = sys.stdin.readline

n = int(read())
rgb = [list(map(int, read().split())) 
        for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]

for i in range(3):
    dp[0][i] = rgb[0][i]

for i in range(1, n):
    dp[i][0] = rgb[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = rgb[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = rgb[i][2] + min(dp[i-1][0], dp[i-1][1])
print(min(dp[n-1]))