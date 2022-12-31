import sys

input = sys.stdin.readline

n = int(input())
road_costs  = list(map(int, input().split()))
oil_prices = list(map(int, input().split()))
res = 0
min_value = oil_prices[0]

for i in range(n - 1):
    min_value = min(min_value, oil_prices[i])
    res += road_costs[i] * min_value
print(res)