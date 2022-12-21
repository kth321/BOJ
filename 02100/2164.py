from collections import deque

Deque = deque()
N = int(input())

for i in range(1, N+1):
    Deque.append(i)

while len(Deque) != 1:
    Deque.popleft()
    Deque.rotate(-1)
print(Deque.pop())