'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''
def countApartment(table, n):
	result = []
	def dfs(i, j, cnt=0):
		if i < 0 or i >= len(table) or\
			j < 0 or j >= len(table) or\
			table[i][j] != '1':
			return cnt
		cnt += 1
		table[i][j] = '0'
		cnt = dfs(i+1, j, cnt)
		cnt = dfs(i-1, j, cnt)
		cnt = dfs(i, j+1, cnt)
		cnt = dfs(i, j-1, cnt)
		return cnt

	for row in range(n):
		for col in range(n):
			if table[row][col] == '1':
				result.append(dfs(row, col))
	return result


n = int(input())
table = [list(input()) for _ in range(n)]
result = countApartment(table, n)
print(len(result))
for apart in sorted(result):
	print(apart)