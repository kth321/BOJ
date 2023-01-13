import sys

read = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        r = a % b
        a, b = b, r
    return a

for t in range(int(read())):
    res = 0
    n, *nums = list(map(int, read().split()))
    for i in range(n - 1):
        for j in range(i + 1, n):
            res += gcd(nums[i], nums[j])
    print(res)