import sys

class stack(object):
    def __init__(self):
        self.items = []
    
    def push(self, x):
        self.items.append(x)
    
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return -1
    
    def size(self):
        return len(self.items)

    def empty(self):
        return 0 if self.items else 1

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            return -1

T = int(sys.stdin.readline())
S = stack()
for _ in range(T):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        S.push(command[1])
    elif command[0] == 'top':
        print(S.top())
    elif command[0] == 'size':
        print(S.size())
    elif command[0] == 'empty':
        print(S.empty())
    elif command[0] == 'pop':
        print(S.pop())