A, B, V = map(int, input().split())
result = (V - B) // (A - B)
print(result + 1) if (V-B) % (A - B) > 0 else print(result)