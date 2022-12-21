import sys
from collections import deque

queue = deque()

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        queue.appendleft(command[1])
    elif command[0] == 'pop':
        print(queue.pop() if queue else -1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(0 if queue else 1)
    elif command[0] == 'front':
        print(queue[-1] if queue else -1)
    elif command[0] == 'back':
        print(queue[0] if queue else -1)