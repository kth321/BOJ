from collections import Counter

_ = input()
L = Counter(map(int, input().split()))
_ = input()
cards = list(map(int, input().split()))
for card in cards:
    if card in L:
        print(L[card], end=' ')
    else:
        print(0, end=' ')