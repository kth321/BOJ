num = input().split()
for i in range(2):
    num[i] = num[i][::-1]
num = list(map(int, num))
if num[0] > num[1]:
    print(num[0])
else:
    print(num[1])
