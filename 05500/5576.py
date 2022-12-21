W = [int(input()) for _ in range(10)]
W.sort()
K = [int(input()) for _ in range(10)]
K.sort()
print(W[-1]+W[-2]+W[-3], K[-1]+K[-2]+K[-3])