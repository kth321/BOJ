import sys

read = sys.stdin.readline

res = 0

_ = int(read())
nums = sorted(list(map(int, read().split())))
while nums:
    res += sum(nums)
    nums.pop()
print(res)