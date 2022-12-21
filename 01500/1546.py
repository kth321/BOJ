n = int(input())
score = list(map(int, input().split()))
max_score = max(score)
sum=0
for s in score:
    sum += s/max_score*100
print(sum/n)