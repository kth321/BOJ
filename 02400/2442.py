N = int(input())
for i in range(N):
    for j in range(i, N-1):
        print(' ', end='')
    for k in range(0, 2*i+1):
        print('*', end='')
    print()