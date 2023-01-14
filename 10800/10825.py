import sys

read = sys.stdin.readline

nums = []
n = int(read())
for _ in range(n):
    nums.append(read().split())
nums.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in range(n):
    print(nums[i][0])