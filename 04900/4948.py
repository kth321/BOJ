import sys

read = sys.stdin.readline

n = 123456
nums = [True] * (2 * n + 1)
for i in range(2, int(n ** 0.5) + 1):
        if nums[i] == True:
            for j in range(i + i, n, i):
                nums[j] = False

while True:
    x = int(read())
    print(sum(nums[x + 1:2 * x + 1]))