from math import floor

n = list(map(int, input().split()))
print(floor((n[0] + 1) * (n[1] + 1) / (n[2] + 1) - 1))