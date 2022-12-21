import sys

try:
    while True:
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
except:
    print('')