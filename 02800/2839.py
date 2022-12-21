N = int(input())
for i in range(N // 5, -1, -1):
    if ((N - i * 5) % 3 == 0):
        print(i + ((N - i * 5) // 3))
        break
    elif i == 0 and N % 3 != 0:
        print(-1)