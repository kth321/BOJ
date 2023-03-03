n = int(input())
nums = list(map(int, input().split()))
max_v = 0
res, cnt = 0, 0


for num in nums:
    if max_v < num:
        max_v = num
        cnt = 0
    else:
        cnt += 1
    res = max(res, cnt)
print(res)