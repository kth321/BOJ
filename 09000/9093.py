for _ in range(int(input())):
    string = input().split()
    for s in range(len(string)):
        string[s] = string[s][::-1]
    print(' '.join(string))