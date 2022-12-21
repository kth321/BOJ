position = {}
for i in range(26):
    position[chr(97 + i)] = -1

s = input()
pos = 0
for i in s:
    if position[i] == -1:
        if i in position:
            position[i] = pos
    pos += 1

result = position.values()
for i in result:
    print(i, end=' ')