n = int(input())

for i in range(n, 3, -1):
    flag = True
    for s in str(i):
        if s != '4' and s != '7':
            flag = False
    if flag:
        print(i)
        exit()