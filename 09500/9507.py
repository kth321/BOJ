fibo = [1, 1, 2, 4] + [None] * 65

def koong(x):
    if fibo[x] != None:
        return fibo[x]
    fibo[x] = koong(x-1) + koong(x-2) + koong(x-3) + koong(x-4)
    return fibo[x]

for _ in range(int(input())):
    print(koong(int(input())))