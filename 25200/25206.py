import sys

read = sys.stdin.readline

grade = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}
w, res = 0, 0

for _ in range(20):
    _, num, g = read().split()
    if g == 'P':
        continue
    w += float(num)
    res += grade[g] * float(num)
print(round(res / w, 5))