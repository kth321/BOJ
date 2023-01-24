import sys

read = sys.stdin.readline

flag = True
pos = read().rstrip()
visited = []
for _ in range(35):
    next_pos = read().rstrip()
    if (abs(ord(pos[0]) - ord(next_pos[0])) == 1 and abs(ord(pos[1]) - ord(next_pos[1])) == 2) or \
        (abs(ord(pos[0]) - ord(next_pos[0])) == 2 and abs(ord(pos[1]) - ord(next_pos[1])) == 1):
        pos = next_pos
    else:
        flag = False
        break
    if next_pos not in visited:
        visited.append(next_pos)
    else:
        flag = False
        break
if (abs(ord(visited[0][0]) - ord(pos[0])) == 1 and  abs(ord(visited[0][1]) - ord(pos[1])) == 2) or \
    (abs(ord(visited[0][0]) - ord(pos[0]) == 2) and abs(ord(visited[0][1]) - ord(pos[1])) == 1):
    pass
else:
    flag = False
print('Valid' if flag else 'Invalid')