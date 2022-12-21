import sys

map_by_num = {}
N, M = map(int, sys.stdin.readline().split())
for i in range(N):
    name = sys.stdin.readline()
    map_by_num[i + 1] = name
map_by_name = {v:k for k, v in map_by_num.items()}

for _ in range(M):
    s = sys.stdin.readline()
    try:
        s = int(s)
        if s in map_by_num:
            print(map_by_num[s][:-1])
    except ValueError:
        if s in map_by_name:
            print(map_by_name[s])