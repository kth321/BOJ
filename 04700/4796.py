i = 1
while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    res = c // b * a
    res += c % b
    print(f'Case {i}: {res}')