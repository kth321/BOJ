n, x = map(int, input().split())

List = list(map(int, input().split()))
for l in List:
    if l < x:
        print(l, end=' ')