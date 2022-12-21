def merge_sort(seq):
    if len(seq) < 2:
        return seq
    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    if left[i:]:
        result.extend(left[i:])
    if right[j:]:
        result.extend(right[j:])
    return result

L = [int(input()) for _ in range(int(input()))]
for i in merge_sort(L):
    print(i)