coins = []
N, K = map(int, input().split())
for _ in range(N):
    coins.append(int(input()))
cnt = 0
coins.reverse()
for coin in coins:
    if K // coin > 0:
        tmp, K = divmod(K, coin)
        cnt += tmp
print(cnt)        