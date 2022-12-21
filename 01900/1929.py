import sys
def prime(x):
    if x < 2:
        return False
    i = 2
    while i *i <=x:
        if x % i == 0:
            return False
        i += 1
    return True

m, n = map(int, sys.stdin.readline().split())
for i in range(m, n+1):
    if prime(i):
        print(i)