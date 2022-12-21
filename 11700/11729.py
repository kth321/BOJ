def Hannoi(n, src ,tmp, to):
    if n == 1:
        print(src, to)
    else:
        Hannoi(n-1, src, to, tmp)
        print(src, to)
        Hannoi(n-1, tmp, src, to)
disk = int(input())
print(2 ** disk - 1)
Hannoi(disk, 1, 2, 3)