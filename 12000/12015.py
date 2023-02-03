from bisect import bisect_left as bl

n, a = int(input()), list(map(int, input().split()))
dp = [0]
for i in range(n):
    if a[i] > dp[-1]:
        dp.append(a[i])
    elif a[i] < dp[-1]:
        tp = bl(dp, a[i])
        if dp[tp] > a[i]:
            dp[tp] = a[i]
print(len(dp) - 1)