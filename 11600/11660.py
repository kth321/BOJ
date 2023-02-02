import sys

read = sys.stdin.readline

n, m = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[1][1] = graph[0][0]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = graph[i-1][j-1] + dp[i][j-1] + dp[i-1][j] -\
                    dp[i-1][j-1]
print()
for l in dp:
    print(*l)
print()
for _ in range(m):
    x1, y1, x2, y2 = map(int, read().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])