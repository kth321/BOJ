s = input()
flag = True
for i in range(len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
        flag = False
print(1 if flag else 0)