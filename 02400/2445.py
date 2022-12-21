N = int(input())

for i in range(N):
    for j in range(i+1):
        print('*', end='')
    for k in range(2*N - 2*i - 2):
        print(' ', end='')
    for l in range(i+1):
        print('*', end='')
    print()
for i in range(N-1):
    for j in range(N-1-i):
        print('*', end='')
    for k in range(2*i + 2):
        print(' ', end='')
    for j in range(N-1-i):
        print('*', end='')
    print()