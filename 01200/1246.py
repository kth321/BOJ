N, M = map(int, input().split())
if M < N:
    N = M
P = [int(input()) for _ in range(M)]
P.sort(reverse=True)
max_value, idx = 0, 0
for i in range(N):
    m = P[i] * (i + 1)
    if m > max_value:
        max_value = m
        idx = P[i]
print(idx, max_value)