from sys import argv

with open(argv[1]) as f:
	data = f.readlines()

out=[]
for case in range(int(data.pop(0))):
	N = int(data.pop(0))

	initbooks = map(int, data.pop(0).split())
	abooks = []
	bbooks = []
	aindices = []
	bindices = []

	for i in range(len(initbooks)):
		if initbooks[i]%2:
			abooks.append(initbooks[i])
			aindices.append(i)
		else:
			bbooks.append(initbooks[i])
			bindices.append(i)

	asorted = sorted(abooks)
	bsorted = sorted(bbooks)[::-1]

	final = [0]*N
	for i in aindices:
		final[i] = asorted.pop(0)
	for i in bindices:
		final[i] = bsorted.pop(0)

	out.append(' '.join(map(str, final)))

with open(argv[2], 'w') as f:
	for i in range(len(out)):
		f.write('Case #%d: %s\n'%(i+1, out[i]))