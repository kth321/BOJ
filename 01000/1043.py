import sys

read = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a in t_people and b in t_people:
        return None
    
    if a in t_people:
        parent[b] = a
    elif b in t_people:
        parent[a] = b
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

n, m = map(int, read().split())
t_num, *t_people = map(int, read().split())
t_people = set(t_people)
parent = [i for i in range(n+1)]
parties = []
res = 0

for _ in range(m):
    p_len, *party = map(int, read().split())
    for i in range(p_len - 1):
        union(party[i], party[i+1])
    parties.append(party)

for party in parties:
    for p in party:
        if find(p) in t_people:
            break
    else:
        res += 1
print(res)