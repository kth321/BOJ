import sys

read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))
if max(nums) < 0:
    print(max(nums))
else:
    s, c = 0, 0
    for i in range(n):
        c += nums[i]
        if c < 0:
            c = 0
        if s < c:
            s = c
    print(s)