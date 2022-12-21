result = []
num = input()
for s in num:
    result.append(s)
result.sort(reverse=True)
for i in result:
    print(i, end='')
print()