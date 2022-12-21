num = []
A, B = map(int, input().split())
for i in range(1, B+1):
    cnt = 0
    while cnt != i:
        num.append(i)
        cnt += 1
print(sum(num[A-1:B]))