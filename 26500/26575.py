import sys

read = sys.stdin.readline

for _ in range(int(read())):
    a, b, c = map(float, read().split())
    print('$', '{:.2f}'.format(round(a * b * c, 2)), sep='')