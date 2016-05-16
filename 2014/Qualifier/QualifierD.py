from sys import argv

with open(argv[1]) as f:
	data = f.read().split('\n')

out=[]
for case in range(int(data.pop(0))):
	print case
	N = int(data.pop(0))
	origNaomi = sorted(map(float, data.pop(0).split()))
	origKen = sorted(map(float, data.pop(0).split()))

	Naomi = origNaomi[:]
	Ken = origKen[:]

	dPoints = 0
	for i in range(N):
		if Ken[0] > Naomi[0]:
			del Ken[-1]
			del Naomi[0]
		else:
			del Ken[0]
			del Naomi[0]
			dPoints += 1

	Naomi = origNaomi[:]
	Ken = origKen[:]

	fPoints = 0
	for i in range(N):
		if Ken[-1] > Naomi[0]:
			for j in Ken:
				if j>Naomi[0]:
					Ken.remove(j)
					break
			del Naomi[0]
		else:
			del Ken[0]
			del Naomi[0]
			fPoints += 1

	out.append(str(dPoints) + ' ' + str(fPoints))

with open(argv[2], 'w') as f:
	for i in range(len(out)):
		f.write('Case #%d: %s\n'%(i+1, out[i]))