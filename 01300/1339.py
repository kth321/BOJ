import sys
from collections import defaultdict

read = sys.stdin.readline

n = int(read())
nums = [list(read().rstrip()) for _ in range(n)]
table = defaultdict(int)
res, idx = 0, 9

for num in nums:
    square_root = len(num) - 1
    for ch in num:
        table[ch] += 10 ** square_root
        square_root -= 1
res_list = sorted(table.values(), reverse=True)
for elem in res_list:
    res += elem * idx
    idx -= 1
print(res)