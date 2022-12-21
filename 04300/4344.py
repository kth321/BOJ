c = int(input())

for i in range(c):
    n, *score = map(int, input().split())
    avg = sum(score)/n
    cnt = 0
    for j in score:
        if j > avg:
            cnt += 1
    result = cnt/n*100
    print('%.3f' %result+"%")