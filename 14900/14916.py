n = int(input())
res = 0

for i in range(n // 5, -1, -1):
  if (n - 5 * i) % 2 == 0:
    print(i + (n - 5 * i) // 2)
    break
  if i == 0 and n % 2 != 0:
    print(-1)