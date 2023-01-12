import sys

read = sys.stdin.readline

while True:
    n, *nums = read().split()
    n = int(n)
    if n == 0:
        break
    nums.sort()
    a = nums[1:n:2]
    b = nums[:n:2]
    if nums.count('0') % 2 == 1:
        a[-1], b[-1] = b[-1], a[-1]

    if '0' in a:
        for i in range(len(a)):
            if a[i] != '0':
                a[0], a[i] = a[i], a[0]
                break
    if '0' in b:
        for i in range(len(b)):
            if b[i] != '0':
                b[0], b[i] = b[i], b[0]
                break
    print(int(''.join(a)) + int(''.join(b)))