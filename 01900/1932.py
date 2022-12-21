N = int(input())
R = []
for i in range(N):
    R.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            R[i][0] = R[i-1][0] + R[i][0]
        elif j == i:
            R[i][j] = R[i-1][j-1] + R[i][j]
        else:
            R[i][j] = max(R[i-1][j-1]+R[i][j], R[i-1][j]+R[i][j])
print(max(R[N-1]))