T = int(input())
stack = []
result = []
last = 1
flag = True
for _ in range(T):
    n = int(input())
    if len(stack) >= 1 and n < stack[-1]:
            flag = False 
    while last <= n:
        stack.append(last)
        result.append('+')
        last += 1
    stack.pop()
    result.append('-')
if flag is True:
    for s in result:
        print(s)
else:
    print('NO')