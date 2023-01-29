n = int(input())
pos = list(map(int, input().split()))
s_pos = sorted(list(set(pos)))
res = {s_pos[i]: i for i in range(len(s_pos))}

for i in range(n):
    pos[i] = res[pos[i]]
print(*pos)