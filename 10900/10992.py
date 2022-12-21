N = int(input())
for i in range(N):
    if i == N-1:
        print('*'*(2*N-1), end='')
    else:
        print(' '*(N-1-i), end='')
        print('*', end='')
        if i != 0:
            print(' '*(2*i-1), end='')
            print('*', end='')
        print()