import sys

read = sys.stdin.readline
n = int(input())
pay = [0] + [list(map(int, read().split())) for _ in range(n)]
dp = [0] * (n + 2)

for i in range(1, n + 1):
    t, p = pay[i]
    dp[i+1] = max(dp[i+1], dp[i])
    if i + t < n + 2:
        dp[i + t] = max(dp[i + t], dp[i] + p)
print(dp[n+1])