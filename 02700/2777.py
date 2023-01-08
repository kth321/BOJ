import sys

read = sys.stdin.readline

for _ in range(int(read())):
    n = int(read())
    tmp = []
    res = []
    idx = 0
    num = 1
    flag = False

    for i in [2, 3, 5, 7]:
        while n % i == 0:
            n //= i
            tmp.append(i)
    if n >= 10:
        tmp.append(n)
    for elem in tmp:
        if elem > 10:
            print(-1)
            flag = True
            break
    if flag:
        continue
    while idx < len(tmp):
        if num * tmp[idx] >= 10:
            res.append(num)
            num = 1
        else:
            num *= tmp[idx]
            idx += 1
    print(len(res) + 1)