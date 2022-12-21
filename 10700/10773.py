stack = []
K = int(input())
for _ in range(K):
    i = int(input())
    if i != 0:
        stack.append(i)
    if i == 0:
        stack.pop()
print(sum(stack))