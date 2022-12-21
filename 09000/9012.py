import sys

T = int(input())

for _ in range(T):
    stack = []
    s = input()
    flag = False
    for i in s:
        try:
            if i == '(':
                stack.append(i)
            elif i == ')':
                stack.pop()
        except IndexError:
            flag = True
    print('NO' if flag is True or len(stack) != 0 else 'YES')