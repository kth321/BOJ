def NGE(nums):
	result = [-1 for _ in range(len(nums))]
	stk = []
	for index in range(len(nums)):
		try:
			while nums[stk[-1]] < nums[index]:
				result[stk.pop()] = nums[index]
		except:
			pass
		stk.append(index)
	return result

input()
print(*NGE(list(map(int, input().split()))))
		