def gcd(x, y):
    while y != 0:
        z = x % y
        x, y = y, z
    return x

a, b = map(int, input().split())
cd = gcd(a, b)
print(cd)
print(a * b // cd)