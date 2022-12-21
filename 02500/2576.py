odd = [int(input()) for _ in range(7)]
odd = list(filter(lambda x: x%2==1, odd))
if not odd:
    print(-1)
else:
    print(sum(odd))
    print(min(odd))