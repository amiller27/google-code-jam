from sys import argv

with open(argv[1]) as f:
	data = f.read().split('\n')

out=[]
for case in range(int(data.pop(0))):
	G1 = int(data.pop(0))-1
	grid1 = list(data.pop(0).split() for i in range(4))
	G2 = int(data.pop(0))-1
	grid2 = list(data.pop(0).split() for i in range(4))

	possibilities = []

	for n in grid1[G1]:
		if n in grid2[G2]:
			possibilities.append(n)

	if len(possibilities)==0:
		out.append('Volunteer cheated!')
	elif len(possibilities)==1:
		out.append(possibilities[0])
	else:
		out.append('Bad magician!')


with open(argv[2], 'w') as f:
	for i in range(len(out)):
		f.write('Case #%d: %s\n'%(i+1, out[i]))