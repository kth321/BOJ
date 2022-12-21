Fib = [0, 1, 1]
def fib(x):
    if x==1:
        return 1
    elif x==2:
        return 1
    try:
        return Fib[x]
    except:
        Fib.append(fib(x-1) + fib(x-2))
        return Fib[x]

x = int(input())
for i in range(x):
    y = int(input())
    if y == 0:
        print(1, 0)
    else:
        print(fib(y-1), fib(y))