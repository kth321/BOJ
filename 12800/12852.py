import sys
max_v = sys.maxsize

n = int(input())
dp = [[0, max_v] for _ in range(n+1)]
res = []
dp[1][1] = 0

for i in range(1, n):
    if i + 1 < n + 1 and dp[i+1][1] > dp[i][1] + 1:
        dp[i+1] = [i, dp[i][1] + 1]
    if i * 2 < n + 1 and dp[i*2][1] > dp[i][1] + 1:
        dp[i*2] = [i, dp[i][1] + 1]
    if i * 3 < n + 1 and dp[i*3][1] > dp[i][1] + 1:
        dp[i*3] = [i, dp[i][1] + 1]

while n >= 1:
    res.append(n)
    n = dp[n][0]
print(len(res) - 1)
print(*res)

# n = int(input())
# dp = [[0, []] for _ in range(n + 1)]
# dp[1][0] = 0
# dp[1][1] = [1]

# for i in range(2, n + 1):
#     dp[i][0] = dp[i-1][0] + 1
#     dp[i][1] = dp[i-1][1] + [i]
#     if i % 3 == 0 and dp[i // 3][0] + 1 < dp[i][0]:
#         dp[i][0] = dp[i // 3][0] + 1
#         dp[i][1] = dp[i // 3][1] + [i]
#     if i % 2 == 0 and dp[i // 2][0] + 1 < dp[i][0]:
#         dp[i][0] = dp[i // 2][0] + 1
#         dp[i][1] = dp[i // 2][1] + [i]

# print(len(dp[n][1]) - 1)
# print(*reversed(dp[n][1]))