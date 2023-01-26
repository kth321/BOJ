from collections import deque

f, s, g, u, d = map(int, input().split())
building = [0] * (f + 1)
building[s] = 1
q = deque([s])
while q:
    x = q.popleft()
    if x == g:
        print(building[x] - 1)
        break
    xu = x + u
    xd = x - d
    if xu <= f and building[xu] == 0:
        building[xu] = building[x] + 1
        q.append(xu)
    if xd > 0 and building[xd] == 0:
        building[xd] = building[x] + 1
        q.append(xd)
else:
    print('use the stairs')