n = int(input())
stairs = [0] +  [int(input()) for _ in range(n)] + [0]
dp = [0] * (n + 2)
dp[1], dp[2] = stairs[1], stairs[1] + stairs[2]

for i in range(3, n + 1):
    dp[i] = max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i] + dp[i-2])
print(dp[n])