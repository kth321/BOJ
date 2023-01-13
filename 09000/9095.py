dp = [0, 1, 2, 4] + [0] * 7

def f(x):
    if dp[x] != 0:
        return dp[x]
    dp[x] = f(x - 3) + f(x - 2) + f(x - 1)
    return dp[x]

f(10)
for T in range(int(input())):
    print(dp[int(input())])