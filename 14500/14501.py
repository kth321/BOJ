import sys

read = sys.stdin.readline

n = int(read())
tp = [tuple(map(int, read().split())) for _ in range(n)]
dp = [0] * n

for i in range(n):
    dp[i + tp[i][0]] = max(dp[i + tp[i][0]], tp[i][1])