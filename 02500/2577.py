count = {}
a = int(input())
b = int(input())
c = int(input())

result = a * b * c
result = str(result)
for i in range(0, 10):
    count[str(i)] = 0
for s in result:
    if s in count:
        count[s] += 1
for i in range(0, 10):
    print(count[str(i)])