from collections import deque

N, M = map(int, input().split())
nums = list(map(int, input().split()))
Deque = deque([x for x in range(1, N+1)])
cnt = 0

while True:
    if nums[0] == Deque[0]:
        Deque.popleft()
        nums.pop(0)
    if not nums:
        break
    idx = Deque.index(nums[0])
    if idx <= len(Deque) // 2:
        Deque.rotate(-idx)
        cnt += idx
    elif idx > len(Deque) // 2:
        Deque.rotate(len(Deque) - idx)
        cnt += len(Deque) - idx
print(cnt)