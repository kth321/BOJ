import sys

read = sys.stdin.readline

for _ in range(int(read())):
    s = read().rstrip()
    print('yes' if 6 <= len(s) <= 9 else 'no')