def binary_search(seq, target, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if target == seq[mid]:
        return True
    elif target < seq[mid]:
        return binary_search(seq, target, low, mid - 1)
    elif target > seq[mid]:
        return binary_search(seq, target, mid + 1, high)

_ = input()
L = sorted(list(map(int, input().split())))
_ = input()
num = list(map(int, input().split()))
for i in num:
    if binary_search(L, i, 0, len(L) - 1):
        print(1)
    else:
        print(0)