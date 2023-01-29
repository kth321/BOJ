# n = int(input())
# if n < 100:
#     print(n)
# else:
#     cnt = 99
#     for i in range(100, n + 1):
#         s = str(i)
#         pos1, pos2 = 0, len(s) - 1
#         res = int(s[pos1]) + int(s[pos2])
#         while pos1 <= pos2:
#             if res != int(s[pos1]) + int(s[pos2]):
#                 break
#             pos1 += 1
#             pos2 -= 1
#         else:
#             cnt += 1
#     print(cnt)
n = int(input())
if n < 100: print(n)
else:
    cnt = 99
    for i in range(100, n + 1):
        s = list(map(int, str(i)))
        if (s[0] - s[1]) == (s[1] - s[2]): cnt += 1
    print(cnt)