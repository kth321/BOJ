class P:
    def __init__(self, info):
        self.age, self.name = info.split()
    def _print(self):
        print(f'{self.age} {self.name}')

def ms(s):
    if len(s) < 2:
        return s
    m = len(s) // 2
    l, r = s[:m], s[m:]
    if len(l) > 1:
        l = ms(l)
    if len(r) > 1:
        r = ms(r)
    res = []
    i, j = 0, 0
    while i < len(l) and j < len(r):
        if l[i].age > r[j].age:
            res.append(r[j])
            j += 1
        elif l[i].age <= r[j].age:
            res.append(l[i])
            i += 1
    if l[i:]:
        res.extend(l[i:])
    if r[j:]:
        res.extend(r[j:])
    return res

L = []
for _ in range(int(input())):
    L.append(P(input()))
for i in ms(L):
    i._print()