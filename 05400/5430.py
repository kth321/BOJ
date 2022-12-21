from collections import deque
import sys
for _ in range(int(sys.stdin.readline())):
    flag = True
    command = sys.stdin.readline()
    n = int(sys.stdin.readline())
    num = sys.stdin.readline()[1:-2].split(',')
    Deque = deque(num)
    for s in command:
        if s == 'R':
            Deque.reverse()
        elif s == 'D':
            try:
                if not Deque[0]:
                    print('error')
                    flag = False
                else:
                    Deque.popleft()
            except IndexError:
                print('error')
                flag = False

    if flag:
        print('[',end='')
        for i in range(len(Deque)):
            if i == len(Deque)-1:
                print(Deque[i], end='')
            else:
                print(Deque[i], end=',')
        print(']')