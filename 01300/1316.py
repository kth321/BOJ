cnt = 0
for _ in range(int(input())):
	target = set()
	exclude = set()
	word = input()
	for s in word:
		if s not in target:
			tmp = s
			target.add(s)
		elif s in target and s == tmp:
			continue
		else:
			exclude.add(s)
	if not exclude:
		cnt += 1
print(cnt)