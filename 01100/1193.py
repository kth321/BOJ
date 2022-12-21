X = int(input())

i = 1
while X - i > 0:
    X -= i
    i += 1
X -= 1
if i % 2 == 0:
    numerator = 1
    denominator = i
    for _ in range(X):
        numerator += 1
        denominator -= 1
else:
    numerator = i
    denominator = 1
    for _ in range(X):
        numerator -= 1
        denominator += 1
print(numerator, '/', denominator, sep='')