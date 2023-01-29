from math import sqrt

n, m = int(input()), int(input())
res = 0
if int(n ** .5) == n ** .5:
    n = int(n ** .5)
else:
    n = int(n ** .5) + 1
tmp = n ** 2
while True:
    if n ** 2 <= m:
        res += n ** 2
    else:
        break
    n += 1

if res == 0:
    print(-1)
else:
    print(res); print(tmp)