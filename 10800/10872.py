def factorial(x):
    if x == 1:
        return 1
    elif x== 0:
        return 1
    else:
        return x * factorial(x-1)

N = int(input())
print(factorial(N))