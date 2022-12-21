num = [0, 0]

x = int(input())
num = num + [None] * (x - 1)
for i in range(2, x + 1):
    tmp = i
    cnt = 0
    while i != 1:
        if num[i] is not None:
            cnt += num[i]
            break
        if i % 3 == 0:
            i = i // 3
        else:
            if i % 2 == 0:
                if num[i//2] > num[i-1]:
                    i -= 1
                else:
                    i = i // 2
            else:
                i -= 1 
        cnt += 1
    num[tmp] = cnt
print(num[-1])

