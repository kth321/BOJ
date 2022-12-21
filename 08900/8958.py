n = int(input())

for i in range(n):
    q = input()
    score = 0
    seq = 1
    for s in q:
        if s == 'O':
            score += seq
            seq +=1
        elif s == 'X':
            seq = 1
    print(score)