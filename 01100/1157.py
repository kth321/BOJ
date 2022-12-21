alphabet = {}

s = input().upper()
for i in s:
    try:
        alphabet[i] += 1
    except KeyError:
        alphabet[i] = 1

value_sorted = sorted(alphabet.values())
if len(alphabet) == 1:
    one_value = alphabet.items()
    for i in one_value:
        print(i[0])
elif value_sorted[-1] == value_sorted[-2]:
    print('?')
else:
    x = 0
    alphabet_items = alphabet.items()
    for a, v in alphabet_items:
        if v > x:
            x = v
            max = a
    print(max)