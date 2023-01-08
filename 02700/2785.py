import sys

read = sys.stdin.readline

n = int(read())
chains = sorted(list(map(int, read().split())))
res = 0

len_chains = len(chains)
idx = 0
min_chain = chains[0]

while len_chains != 1:
    if min_chain >= 1:
        min_chain -= 1
        len_chains -= 1
        res += 1
    else:
        len_chains -= 1
        idx += 1
        min_chain = chains[idx]
print(res)
