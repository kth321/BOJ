dp = [0] + [1, 1, 2, 3, 5] + [0] * 35
for i in range(6, 41):
    dp[i] = dp[i-1] + dp[i-2]

n = int(input())
print(dp[n], n-2)