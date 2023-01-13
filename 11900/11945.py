import sys

read = sys.stdin.readline

n, m = map(int, read().split())
for _ in range(n):
    print(input()[::-1])