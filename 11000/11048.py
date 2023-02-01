import sys

read = sys.stdin.readline

n, m = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = graph[0][0]

for i in range(1, m):
    dp[0][i] = dp[0][i-1] + graph[0][i]
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + graph[i][0]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + graph[i][j]
print(dp[-1][-1])