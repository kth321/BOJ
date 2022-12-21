T = int(input())

for i in range(T):
    s = input().split()
    l, character = s
    for j in character:
        for k in range(int(l)):
            print(j, end='')
    print()