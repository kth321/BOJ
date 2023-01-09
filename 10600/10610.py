n = sorted(list(map(int, list(input()))), reverse=True)
if 0 not in n or sum(n) % 3 != 0:
    print(-1)
else:
    print(''.join(list(map(str, n))))