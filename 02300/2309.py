a = []
def solution(x):
    h_sum = sum(x)
    for i in range(8):
        for j in range(i+1, 9):
            if h_sum - (x[i] + x[j]) == 100:
                x.pop(a.index(a[i]))
                x.pop(a.index(a[j-1]))
                return x
for _ in range(9):
    a.append(int(input()))
solution(a)
a.sort()
for h in a:
    print(h)