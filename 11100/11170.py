dp = [0] * 1_000_001
dp[0] = 1

for i in range(1, 1_000_001):
    x = str(i).count('0')
    dp[i] = dp[i-1] + x

for i in range(int(input())):
    n, m = map(int, input().split())
    if n == 0:
        print(dp[m])
    else:
        print(dp[m] - dp[n-1])