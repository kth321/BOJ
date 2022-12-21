from collections import deque

N, K = map(int, input().split())
queue = deque(range(1,N+1))
print('<', end='')
while queue:
    queue.rotate(-K+1)
    if len(queue) != 1:
        print(queue.popleft(), end=', ')
    else:
        print(queue.popleft(), end='')
print('>')