x=int(input())

for i in range(0,x*2):
    if i%2==0:
        for j in range(0,x):
            if j%2==0:
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    else:
        for j in range(0,x):
            if j%2==0:
                print(' ',end='')
            else:
                print('*',end='')
        print('')