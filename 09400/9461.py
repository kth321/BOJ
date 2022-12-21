for _ in range(int(input())):
    n = int(input())
    m = [1, 1, 1] + [None] * (n - 3)
    for i in range(3, n):
        m[i] = m[i-2] + m[i-3]
    print(m[n-1])