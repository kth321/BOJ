vowel = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
for _ in range(int(input())):
    cnt_v, cnt_s = 0, 0
    string = input()
    for s in string:
        if s in vowel:
            cnt_v += 1
        elif s not in vowel and s != ' ':
            cnt_s += 1
    print(cnt_s, cnt_v)