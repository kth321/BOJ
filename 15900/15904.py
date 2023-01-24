s = input()
ucpc = list('UCPC')
i = 0

for symbol in ucpc:
    if symbol in s:
        i += 1
        s = s[s.index(symbol) + 1:]
    else:
        print('I hate UCPC')
        break

if i == 4:
    print('I love UCPC')