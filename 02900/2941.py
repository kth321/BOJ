croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
string = input()
for i in croa:
    if len(string.split(i)) >= 2:
        cnt += len(string.split(i)) - 1
print(len(string) - cnt)
