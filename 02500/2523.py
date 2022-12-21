x=int(input())

for i in range(1,x+1):
    for j in range(0,i):
        print('*',end='')
    print('')
for i in range(x-1,0,-1):
    for j in range(0,i):
        print('*',end='')
    print('')
