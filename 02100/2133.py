N = int(input())
tile = [1, 3] + [None] * (N // 2 - 1)

def make_tile(x):
    if x == 2:
        return 3
    if tile[x // 2] is not None:
        return tile[x // 2]
    sum = 3 * make_tile(x-2)
    for i in tile[:x//2-1]:
        sum += 2 * i
    tile[x // 2] = sum
    return tile[x // 2]

if N %2 == 1:
    print(0)
else:
    print(make_tile(N))
