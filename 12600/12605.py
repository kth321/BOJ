import sys

read = sys.stdin.readline

for i in range(int(read())):
    x = read().split()
    print(f'Case #{i+1}:', *x[::-1])