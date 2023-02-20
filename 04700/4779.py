import sys

read = sys.stdin.readline

def sol(pos, n):
    if n == 1:
        return None
    n //= 3
    for i in range(n, 2 * n):
        res[pos+i] = ' '
    sol(pos, n)
    sol(pos + 2*n, n)

while True:
    n = read().rstrip()
    if not n:
        break
    n = 3 ** int(n)
    res = ['-'] * n
    sol(0, n)
    print(''.join(res))