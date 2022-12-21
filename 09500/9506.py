def perfect(x):
    num = []
    for i in range(1, x):
        if x % i == 0:
            num.append(i)
    if sum(num) == x:
        print(x, '=', end=' ')
        for j in num:
            if j == num[-1]:
                print(j)
            else:
                print(j, end=' + ')
    else:
        print(f'{x} is NOT perfect.')

while True:
    x = int(input())
    if x == -1:
        break
    perfect(x)