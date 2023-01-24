# import itertools
# N,M = map(int,input().split())
# list1 = list(map(str,range(1,N+1)))
# 
# print("\n".join(list(map(" ".join,itertools.product(list1,repeat=M)))))

def seQuence(n, m):
	outputs = []
	elements = list(range(1, n+1))
	def dfs(path):
		if len(path) == m:
			outputs.append(path)
			return
		for i in range(len(elements)):
			dfs(path+[i+1])
	dfs([])
	return outputs

n, m = map(int, input().split())
results = seQuence(n, m)
for result in results:
	print(*result)