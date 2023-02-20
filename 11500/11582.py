import sys

read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))
k = int(read())

for i in range(0, n, n // k):
    nums[i:i + n//k] = sorted(nums[i:i + n//k])
print(*nums)