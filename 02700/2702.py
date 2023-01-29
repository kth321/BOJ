from math import gcd

for _ in range(int(input())):
    a, b = map(int, input().split())
    cd = gcd(a, b)
    print(a * b // cd, cd)