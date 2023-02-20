k = int(input())
cnt = 0
while k != 1:
    tmp = 1
    while tmp << 1 < k:
        tmp <<= 1
    k -= tmp
    cnt += 1
print(1 if cnt % 2 == 1 else 0)