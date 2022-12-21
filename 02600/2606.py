computer = int(input())
link = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    if link:
        flag = False
        for i in link:
            if a in i or b in i:
                i.add(a)
                i.add(b)
                flag = True
        if not flag:
            link.append({a, b})
    else:
        link.append({a, b})

for i in link:
    if 1 in i:
        print(len(i)-1)
for i in link:
    print(i)