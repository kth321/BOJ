for _ in range(int(input())):
    s = input().lower()
    flag = True
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            flag = False
    if flag:
        print('Yes')
    else:
        print('No')