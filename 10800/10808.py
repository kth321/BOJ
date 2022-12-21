alphabet = {chr(97+i):0 for i in range(26)}
s = input()
for i in s:
    if i in alphabet:
        alphabet[i] += 1
for i in alphabet.values():
    print(i, end=' ')