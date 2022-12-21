import sys

N, K = map(int, sys.stdin.readline().split())
nums = [False, False] + [True] * (N-1)
cnt = 0

while True:
    min_value = nums.index(True)
    for i in range(min_value, N+1, min_value):
        if nums[i]:
            nums[i] = False
            cnt += 1
            if cnt == K:
                print(i)
                break
    if cnt == K:
        break