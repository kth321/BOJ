while True:
    num = list(map(int, input().split()))
    if num[0] == 0 and num[1] == 0 and num[2] == 0:
        break
    num.sort()
    if num[0]**2 + num[1]**2 == num[2]**2:
        print('right')
    else:
        print('wrong')