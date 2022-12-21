from collections import deque

for _ in range(int(input())):
    N, M = map(int, input().split())
    Deque = deque(enumerate(list(map(int, input().split()))))
    cnt = 0
    while True:
        max_value = 0
        for i in Deque:
            if i[1] > max_value:
                max_value = i[1]
        while Deque[0][1] != max_value:
            Deque.rotate(-1)
        x = Deque.popleft()
        cnt += 1
        if x[0] == M:
            break
    print(cnt)