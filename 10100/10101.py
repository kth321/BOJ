a = [int(input()) for _ in range(3)]

if a[0] == a[1] == a[2] == 60:
    print('Equilateral')
elif sum(a) == 180 and \
    a[0] == a[1] or \
    a[1] == a[2] or \
    a[2] == a[0]:
        print('Isosceles')
elif sum(a) == 180:
    print('Scalene')
else:
    print('Error')