num = [None, 1, 2, 4] + [None] * 7

def f(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    if num[x] != None:
        return num[x]
    num[x] = f(x-3) + f(x-2) + f(x-1)
    return num[x]

for _ in range(int(input())):
    print(f(int(input())))