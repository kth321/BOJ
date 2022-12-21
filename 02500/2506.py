_ = input()
L = list(map(int, input().split()))

sum = 0
score = 0
for i in range(len(L)):
    if L[i] == 1:
        score += 1
    elif L[i] == 0:
        score = 0
    sum += score
print(sum)