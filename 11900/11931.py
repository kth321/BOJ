import sys

read = sys.stdin.readline

n = int(read())
nums = sorted(list(int(read()) for _ in range(n)), reverse=True)
for i in range(n):
    print(nums[i])