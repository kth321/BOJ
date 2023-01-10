res = 0

while True:
    try:
        input()
        res += 1
    except EOFError:
        break
print(res)