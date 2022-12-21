fibonacci = [0, 1, 1]
def fibo(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    try:
        if fibonacci[x] != 0:
            return fibonacci[x]
    except IndexError:
        fibonacci.append(fibo(x - 1) + fibo(x - 2))
    return fibonacci[x]

n = int(input())
print(fibo(n))