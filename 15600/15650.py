def seQence(n, m):
	outputs = []
	def dfs(index, elements):
		if len(elements) == m:
			outputs.append(elements)
			return
		for i in range(index, n):
			dfs(i+1, elements+[i+1])
	dfs(0, [])
	return outputs

n, m = map(int, input().split())
results = seQence(n, m)
for result in results:
	for element in result:
		print(element, end=' ')
	print()

