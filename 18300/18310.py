n = int(input())
nums = sorted(list(map(int, input().split())))
print(nums[(n - 1)// 2])