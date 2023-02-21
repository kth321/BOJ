import sys

read = sys.stdin.readline

nums = []
for i in range(int(read())):
    nums.append([i] + list(read().split()))
    nums[i][1] = int(nums[i][1])
for num in sorted(nums, key=lambda x: (x[1], x[0])):
    print(*num[1:])