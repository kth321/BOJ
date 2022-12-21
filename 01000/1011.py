x = int(input())

for i in range(x):
    a, b = map(int, input().split())
    d = abs(a - b)
    sub = 1
    cnt = 0
    while d > 0:
        for _ in range(2):
            d = d - sub
            cnt += 1
            if d <= 0:
                break
        if cnt%2 == 0:
            sub += 1
    print(cnt)