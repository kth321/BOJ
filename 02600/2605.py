N = int(input())
num = list(map(int, input().split()))
student = []
for i in range(0, N):
    if i == 0:
        student.append(1)
    else:
        student.insert(len(student) - num[i], i+1)
for s in student:
    print(s, end=' ')