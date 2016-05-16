from sys import argv

with open(argv[1]) as f:
	data = f.read().split('\n')

out=[]
for case in range(int(data.pop(0))):
	print case+1
	N = int(data.pop(0))
	strings = list(data.pop(0) for i in range(N))

	letters = [strings[0][0]]
	counts = [[1]]

	for letter in strings[0][1:]:
		if letter == letters[-1]:
			counts[-1][-1]+=1
		else:
			letters.append(letter)
			counts[-1].append(1)

	# print N
	# print strings
	# print letters
	# print counts

	failed=False
	for s in strings[1:]:
		i=0
		counts.append(list([0 for j in range(len(letters))]))
		for letterI, letter in enumerate(s):
			if letter == letters[i]:
				counts[-1][i]+=1
			elif i<len(letters)-1 and letter==letters[i+1]:
				i+=1
				counts[-1][i]+=1
			else:
				out.append("Fegla Won")
				failed=True
				break
		if failed:
			break
		if filter(lambda x:x==0, counts[-1]):
			out.append("Fegla Won")
			failed=True
			break
	if failed:
		continue

	# print letters
	# print counts




	deltas = 0
	for i in range(len(letters)):
		if len(letters)%2:
			median = sorted(counts[j][i] for j in range(N))[(N-1)/2]
		else:
			median = int(round(sum(sorted(counts[j][i] for j in range(N))[N/2-1:N/2+1])/2.0))

		for sIndex in range(N):
			deltas+=abs(counts[sIndex][i] - median)
	out.append(deltas)


with open(argv[2], 'w') as f:
	for i in range(len(out)):
		f.write('Case #%d: %s\n'%(i+1, out[i]))