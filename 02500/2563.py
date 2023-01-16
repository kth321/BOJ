import sys

read = sys.stdin.readline
paper = [[0] * 100 for _ in range(100)]
cnt = 0

for _ in range(int(read())):
    x, y = map(int, read().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

for line in paper:
    cnt += line.count(1)
print(cnt)