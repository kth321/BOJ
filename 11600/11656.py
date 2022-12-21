s = input()
suffix = [s[i:] for i in range(len(s))]
suffix.sort()
for i in suffix:
    print(i)