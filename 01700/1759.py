from itertools import combinations

vowels = list('aeiou')
l, c = map(int, input().split())
arr = sorted(input().split())

for pwd in combinations(arr, l):
    cnt = 0
    for c in pwd:
        if c in vowels:
            cnt += 1
    if 1 <= cnt <= l - 2:
        print(''.join(pwd))