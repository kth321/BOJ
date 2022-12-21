count = {}
for i in range(0, 10):
    x = int(input())
    if x%42 in count:
        count[x%42] += 1
    else:
        count[x%42] = 1
print(len(count))