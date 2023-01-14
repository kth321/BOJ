import sys

read = sys.stdin.readline

lines = [int(read()) for _ in range(int(read()))]
max_val = lines[-1]
cnt = 1

for i in range(len(lines) - 1, -1, -1):
    if max_val < lines[i]:
        max_val = lines[i]
        cnt += 1

print(cnt)