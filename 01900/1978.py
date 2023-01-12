import sys

read = sys.stdin.readline

def sol(x):
    if x == 1:
        return False
    cnt = 0
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            cnt += 1
        if cnt >= 1:
            return False
    return True

_ = int(read())
nums = list(map(int, read().split()))
cnt = 0

for num in nums:
    if sol(num):
        cnt += 1
print(cnt)