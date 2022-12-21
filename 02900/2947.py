n = list(map(int, input().split()))
while n != sorted(n):
    for i in range(5):
        try:
            if n[i] > n[i+1]:
                n[i], n[i+1] = n[i+1], n[i]
                for j in n:
                    print(j, end=' ')
                print()
        except IndexError:
            break