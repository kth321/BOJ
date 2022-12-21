score = [int(input()) for _ in range(8)]
s = 0
res = []
score = sorted(enumerate(score), key=lambda x:x[1])
for i in range(5):
    s += score[7-i][1]
    res.append(score[7-i][0]+1)

print(s)
for i in sorted(res):
    print(i, end=' ')