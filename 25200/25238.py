defense, per = map(int, input().split())
defense *= (100 - per) / 100
print(defense)
if defense >= 100:
    print(0)
else:
    print(1)