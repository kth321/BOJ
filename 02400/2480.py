a = 0
cnt = 0
L = list(map(int, input().split()))
L.sort()
for i in range(2):
    if L[i+1] == L[i]:
        cnt += 1
        a = L[i]
if cnt == 2:
    print(10000 + a * 1000)
elif cnt == 1:
    print(1000 + a * 100)
elif cnt == 0:
    print(max(L) * 100)