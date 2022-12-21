num = []
for _ in range(5):
    num.append(int(input()))
print(int(sum(num) / 5))
num.sort()
print(num[2])