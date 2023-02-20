def sol(r, c, n):
    global res
    if n == 0:
        return None
    n -= 1
    if r < 2 ** n and c < 2 ** n:
        sol(r, c, n)
    elif r < 2 ** n and c >= 2 ** n:
        res += 2 ** (n*2)
        c -= 2 ** n
        sol(r, c, n)
    elif r >= 2 ** n and c < 2 ** n:
        res += 2 ** (n*2) * 2
        r -= 2 ** n
        sol(r, c, n)
    else:
        res += 2 ** (n*2) * 3
        r -= 2 ** n
        c -= 2 ** n
        sol(r, c, n)
n, r, c = map(int, input().split())
res = 0
sol(r, c, n)
print(res)