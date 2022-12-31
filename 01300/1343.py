boards = input().split('.')
res = []
for board in boards:
    if len(board) % 2 != 0:
        res = [-1]
        break
    else:
        res.append('AAAA' * (len(board) // 4) + \
            'BB' * ((len(board) % 4) // 2))

if -1 not in res:
    print('.'.join(res))
else:
    print(*res)