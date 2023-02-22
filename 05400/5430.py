from collections import deque
import sys

read = sys.stdin.readline

for _ in range(int(read())):
    command = read().rstrip()
    n = read().rstrip()
    nums = read().rstrip()[1:-1].split(',')
    R = False
    e_flag = False

    nums = deque(nums)
    if n == '0':
        nums = deque()
    for s in command:
        if s == 'R':
            if R: R = False
            else: R = True
        else:
            if not nums:
                print('error')
                e_flag = True
                break
            if R:
                nums.pop()
            else:
                nums.popleft()
    if not e_flag:
        if R:
            nums = reversed(nums)
        print('[' + ','.join(nums) + ']')