import sys

read = sys.stdin.readline
_ = read().strip()
A = sorted(list(map(int, read().split())))
B = sorted(list(map(int, read().split())), reverse=True)
res = 0

for a, b in zip(A, B):
    res += a * b
print(res)