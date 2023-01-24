result = "draw"
questionScore = [100, 100, 200, 200, 300, 300, 400, 400, 500]
getScore = list(map(int, input().split()))
if sum(getScore) >= 100:
	for scoreIndex, score in enumerate(getScore):
		if score > questionScore[scoreIndex]:
			result = "hacker"
			break
else:
	result = "none"
print(result)