import sys

read = sys.stdin.readline

table = {'CU': 'see you',
        ':-)': 'I’m happy',
        ':-(': 'I’m unhappy',
        ';-)': 'wink',
        ':-P': 'stick out my tongue',
        '(~.~)': 'sleepy',
        'TA': 'totally awesome',
        'CCC': 'Canadian Computing Competition',
        'CUZ': 'because',
        'TY': 'thank-you',
        'YW': "you’re welcome",
        'TTYL':	'talk to you later'}

while True:
    s = read().strip()
    print(table[s] if s in table else s)
    if s == 'TTYL':
        break