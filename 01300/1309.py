n = int(input())
dp = [[0] * 3 for _ in range(n + 1)]
for i in range(3):
    dp[1][i] = 1
for i in range(2, n + 1):
    s = sum(dp[i-1])
    dp[i][0] = s % 9901
    dp[i][1] = (s - dp[i-1][1]) % 9901
    dp[i][2] = (s - dp[i-1][2]) % 9901
print(sum(dp[n]) % 9901)