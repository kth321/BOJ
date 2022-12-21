result = []
s = input()
for i in range(len(s)):
    num = ord(s[i])
    if 65 <= num <= 77:
        result.append(chr(num+13))
    elif 78 <= num <= 90:
        result.append(chr(num-13))
    elif 97 <= num <= 109:
        result.append(chr(num+13))
    elif 110 <= num <= 122:
        result.append(chr(num-13))
    else:
        result.append(s[i])
for i in result:
    print(i, end='')