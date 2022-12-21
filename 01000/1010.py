def factorial(n):
    x = 1
    for i in range(n):
        x = x * (i + 1)
    return x

def combination(x, y):
    return int(factorial(y) / (factorial(x) * factorial(y - x)))

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(combination(a, b))