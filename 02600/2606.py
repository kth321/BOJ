from collections import deque
import sys

read = sys.stdin.readline

def bfs(start_v=1):
	q = deque([start_v])
	check = []
	while q:
		v = q.popleft()
		for w in table[v]:
			if w not in check:
				q.append(w)
		if v not in check:
			check.append(v)
	return len(check) - 1

n, m = int(read()), int(read())
table = {i+1: [] for i in range(n)}
for _ in range(m):
	s, e = map(int, read().split())
	table[s].append(e)
	table[e].append(s)
print(bfs())