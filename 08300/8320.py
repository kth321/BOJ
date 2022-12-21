from math import sqrt

N = int(input())
sum = 0
for i in range(1, N+1):
    for j in range(1, int(sqrt(i)) + 1):
        if i % j == 0:
            sum += 1
print(sum)