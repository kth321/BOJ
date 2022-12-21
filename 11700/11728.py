L = []

_ = input()
L.extend(list(map(int, input().split())))
L.extend(list(map(int, input().split())))

for i in sorted(L):
    print(i, end=' ')