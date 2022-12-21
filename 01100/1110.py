cnt = 0
n = int(input())
num = n

while True:
    last = n%10
    new = n//10 + last
    n = last*10 + new%10
    cnt += 1
    if n == num:
        break

print(cnt)