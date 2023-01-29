n, m = map(int, input().split())
c = sorted(list(map(int, input().split())))
res = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            s = c[i] + c[j] + c[k]
            if s <= m:
                res = max(res, s)
print(res)