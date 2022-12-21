score = [0 for _ in range(5)]

for i in range(5):
    score[i] = sum(list(map(int, input().split())))
max = max(score)
print(score.index(max) + 1, max)