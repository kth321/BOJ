import re

input()
S = re.sub('[JAV]+', '', input())
print(S if S else 'nojava')