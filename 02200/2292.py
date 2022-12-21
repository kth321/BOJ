N = int(input())
if N == 1:
    print(1)
else:
    N -= 1
    cnt = 1
    while N >0:
        N -= 6 * cnt
        cnt += 1
    print(cnt)