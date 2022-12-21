dict = {'ABC':3, 'DEF':4, 'GHI':5, 'JKL':6, 'MNO':7, 'PQRS':8, 'TUV':9, 'WXYZ':10}
s = input()
time_sum = 0
for number in s:
    for letter, time in dict.items():
        if number in letter:
            time_sum += time
print(time_sum)