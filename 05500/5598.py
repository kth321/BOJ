string = input()
for s in string:
    if s == 'A':
        print('X', end='')
    elif s == 'B':
        print('Y', end='')
    elif s == 'C':
        print('Z', end='')
    else:
        print(chr(ord(s) - 3), end='')