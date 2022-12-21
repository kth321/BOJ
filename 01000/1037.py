N = int(input())
x = list(map(int, input().split()))
x.sort()
if N %2 == 0:
    print(x[0] * x[-1])
else:
    print((x[N // 2] ** 2))