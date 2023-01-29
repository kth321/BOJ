p, k = map(int, input().split())
for i in range(2, p):
    if p % i == 0:
        if p >= k and p // i >= k:
            print('GOOD')
        else:
            print('BAD', i)
        exit()