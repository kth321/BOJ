N = int(input())

for i in range(N):
    for j in range(i):
        print(' ', end='')
    for k in range(i, N):
        print('*', end='')
    print()