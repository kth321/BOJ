for _ in range(3):
    cnt = 0
    s = input().split()
    for i in s:
        if i == '1':
            cnt += 1
    if cnt == 0:
        print('D')
    elif cnt == 1:
        print('C')
    elif cnt == 2:
        print('B')
    elif cnt == 3:
        print('A')
    elif cnt == 4:
        print('E')