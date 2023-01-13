def check(n, k):
    sieve = [True] * (n + 1)
    cnt = 0

    for i in range(2, n + 1):
        if sieve[i] == True:
            for j in range(i, n + 1, i):
                if sieve[j] == True:
                    cnt += 1
                    sieve[j] = False
                    if cnt == k:
                        return j

n, k = map(int, input().split())
print(check(n, k))