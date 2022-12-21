for _ in range(int(input())):
    res = 0
    s = input().split()
    num, *s = s
    num = float(num)
    for i in s:
        if i == '@':
            num *= 3
        elif i == '%':
            num += 5
        elif i == '#':
            num -= 7
    print('%.2f' %num)