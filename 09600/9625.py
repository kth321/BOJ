fibo = [0, 1, 1] + [None] * 43

def Fibo(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    if fibo[x] != None:
        return fibo[x]
    fibo[x] = Fibo(x-1) + Fibo(x-2)
    return fibo[x]
n = int(input())
Fibo(n)
print(fibo[n-1], fibo[n])