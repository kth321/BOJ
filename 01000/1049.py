N, M = map(int, input().split())
package, piece = 1000, 1000
sum = 0
for _ in range(M):
    a, b = map(int, input().split())
    package = a if a < package else package
    piece = b if b < piece else piece

if 6 * piece < package:
    sum = N * piece
else:
    pack, N = divmod(N, 6)
    sum = pack * package
    x = package if N * piece > package else N * piece
    sum += x
print(sum)