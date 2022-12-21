N, *L = input().split()
N = int(N)
while len(L) != N:
    L.extend(input().split())

for i in range(len(L)):
    L[i] = L[i].strip('0')
    L[i] = L[i][-1::-1]

L = list(map(int, L))
for i in L:
    print(i)