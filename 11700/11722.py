from bisect import bisect_left as bl

n, a = int(input()), list(map(lambda x: -x, map(int, input().split())))
dp = [-1001]
for i in range(n):
    if a[i] > dp[-1]:
        dp.append(a[i])
    elif a[i] < dp[-1]:
        tp = bl(dp, a[i])
        if a[i] < dp[tp]:
            dp[tp] = a[i]
print(len(dp) - 1)