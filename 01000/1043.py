import sys

read = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

n, m = map(int, read().split())
truth = list(map(int, read().split()))[1:]
parent = [i for i in range(n+1)]
parties = []
res = 0
for _ in range(m):
    party = list(map(int, read().split()))[1:]
    first = party[0]
    for person in party[1:]:
        union(first, person)
    parties.append(party)
for party in parties:
    for t in truth:
        if find(party[0]) == find(t):
            break
    else:
        res += 1
print(res)