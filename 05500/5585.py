import sys
coins = [500, 100, 50, 10, 5, 1]
cnt = 0
money = 1000 - int(sys.stdin.readline())
for coin in coins:
    cnt += money // coin
    money %= coin
print(cnt)