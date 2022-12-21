h = input()
pos = len(h) - 1
sum = 0
for i in h:
    if i == 'A':
        sum += 10 * (16 ** pos)
    elif i == 'B':
        sum += 11 * (16 ** pos)
    elif i == 'C':
        sum += 12 * (16 ** pos)
    elif i == 'D':
        sum += 13 * (16 ** pos)
    elif i == 'E':
        sum += 14 * (16 ** pos)
    elif i == 'F':
        sum += 15 * (16 ** pos)
    else:
        sum += int(i) * (16 ** pos)
    pos -= 1
print(sum)