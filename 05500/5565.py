price = [int(input()) for _ in range(10)]
sum_price, *price = price
print(sum_price - sum(price))