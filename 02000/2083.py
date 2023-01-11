import sys

read = sys.stdin.readline

while True:
    a, b, c = read().split()
    if a == '#' and b == '0' and c == '0':
        break
    b, c = map(int, (b, c))
    if b > 17 or c >= 80:
        print(a + ' Senior')
    else:
        print(a + ' Junior')