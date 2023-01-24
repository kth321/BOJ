import sys

read = sys.stdin.readline

S = read().rstrip()
flag = True
res, stk = [], []
for s in S:
    if s == '>':
        flag = True
        continue
    elif s == '<':
        flag = False
        while stk:
            res.append(stk.pop())
    if flag:
        stk.append(s)
    else:
        res.append(s)
while stk:
    res.append(stk.pop())
print(''.join(res))