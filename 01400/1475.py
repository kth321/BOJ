num = {str(x):0 for x in range(10)}
s = input()
for i in s:
    if i in num:
        num[i] += 1
_69 = num['6'] + num['9']
if _69 % 2 == 0:
    _69 //= 2
else:
    _69 = _69 // 2 + 1
del(num['6']); del(num['9'])
if _69 > max(num.values()):
    print(_69)
else:
    print(max(num.values()))