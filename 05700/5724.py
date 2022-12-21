while True:
    i = int(input())
    sum = 0
    if i == 0:
        break
    for j in range(i+1):
        sum += j ** 2
    print(sum)