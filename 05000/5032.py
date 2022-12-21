e, f, c = map(int, input().split())
i = e + f
r = 0
while i >= c:
    tmp, i = divmod(i, c)
    i += tmp
    r += tmp
print(r)