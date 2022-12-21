from collections import deque

N, K = map(int, input().split())
Deque = deque([x for x in range(N, 0, -1)])
print('<', end='')
while Deque:
    Deque.rotate(K-1)
    print(Deque.pop(), end='')
    if Deque:
        print(', ', end='')
print('>')