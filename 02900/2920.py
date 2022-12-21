m = list(map(int, input().split()))
if sorted(m) == m:
    print('ascending')
elif sorted(m, reverse=True) == m:
    print('descending')
else:
    print('mixed')