from collections import defaultdict, deque

def dfs(result_dfs, start_v):
	if start_v not in result_dfs:
		result_dfs.append(start_v)
		for vertex in table[start_v]:
			dfs(result_dfs, vertex)
	return result_dfs

def bfs(result_bfs, start_v):
	q = deque()
	q.append(start_v)
	while q:
		v = q.popleft()
		for w in table[v]:
			if w not in result_bfs:
				q.append(w)
		if v not in result_bfs:
			result_bfs.append(v)
	return result_bfs


N, M, V = map(int, input().split())

table = defaultdict(list)

for _ in range(M):
	start_v, end_v = map(int, input().split())
	table[start_v].append(end_v)
	table[end_v].append(start_v)
for sort_iterator in table:
	table[sort_iterator].sort()

result_dfs = dfs([], V)
result_bfs = bfs([], V)
print(*result_dfs)
print(*result_bfs)