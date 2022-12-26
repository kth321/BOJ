nums = input()
first_num = nums[0]
s = False
res = 0

for i in range(len(nums)):
  if nums[i] != first_num:
    s = True
  elif s is True and nums[i] == first_num:
    res += 1
    s = False

if s is True:
    res += 1

print(res)