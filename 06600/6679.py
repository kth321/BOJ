def cal(x, op):
    res = 0
    while x > 0:
        res += x % op
        x //= op
    return res
for i in range(1000, 10000):
    if cal(i, 10) == cal(i, 12) == cal(i, 16):
        print(i)