N = int(input())

for i in range(N):
    for j in range(N-1-i):
        print(' ', end='')
    print('*', end='')
    if i != 0:
        for k in range(2*i-1):
            print(' ', end='')
        print('*', end='')
    print()