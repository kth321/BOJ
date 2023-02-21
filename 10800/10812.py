import sys

read = sys.stdin.readline

n, m = map(int, read().split())
nums = [i for i in range(n+1)]

for _ in range(m):
    i, j, k = map(int, read().split())
    nums[i:j+1] = nums[k:j+1] + nums[i:k]
print(*nums[1:])