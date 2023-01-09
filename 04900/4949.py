import re

table = {
	')': '(',
	']': '['
}

def balanceWorld(input: str):
	regex = "[^\[\]\(\)]"
	input = re.sub(regex, '', input)
	stk = []
	for char in input:
		if char not in table:
			stk.append(char)
		elif stk and table[char] == stk[-1]:
			stk.pop()
		else:
			return "no"
	return "yes" if not stk else "no"

while True:
	sentance = input()
	if sentance == '.':
		break
	print(balanceWorld(sentance))