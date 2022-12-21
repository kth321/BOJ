listened = set()
seened = set()
N, M = map(int, input().split())
for _ in range(N):
    listened.add(input())
for _ in range(M):
    seened.add(input())
dutbo = sorted(listened.intersection(seened))
print(len(dutbo))
for i in dutbo:
    print(i)