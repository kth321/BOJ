import sys
queue = []
N = int(sys.stdin.readline())
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        queue.insert(0, command[1])
    elif command[0] == 'front':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(0 if queue else 1)
    elif command[0] == 'back':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'pop':
        if queue:
            print(queue.pop())
        else:
            print(-1)