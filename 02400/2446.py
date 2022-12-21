N = int(input())

for i in range(N):
    for k in range(i):
        print(' ', end='')
    for j in range(2*N-2*i-1):
        print('*', end='')
    print()
for i in range(N-1):
    for k in range(N-i-2):
        print(' ', end='')
    for j in range(2*i+3):
        print('*', end='')
    print()