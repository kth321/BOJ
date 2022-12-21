n = int(input())
people = list(map(int, input().split()))
people.sort()
time = 0
for i in range(n):
    time += sum(people)
    people.pop()
print(time)