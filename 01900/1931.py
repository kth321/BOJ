timetable = []
res = 1
N = int(input())

for _ in range(N):
    timetable.append(list(map(int, input().split())))

timetable.sort(key=lambda x: (x[1], x[0]))

prev = timetable[0][1]
for t in timetable[1:]:
    if prev <= t[0]:
        prev = t[1]
        res += 1
print(res)