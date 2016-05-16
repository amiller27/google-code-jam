from sys import argv

with open(argv[1]) as f:
	data = f.read().split('\n')

out=[]
for case in range(int(data.pop(0))):
	N = int(data.pop(0))
	matrix = list(data.pop(0).split() for i in range(N**2))
	done=False
	for row in matrix:
		if set(map(int, row))!=set(range(1, N**2+1)):
			out.append('No')
			done=True
			break
	if done:
		continue
	
	for i in range(N**2):
		if set(map(int, list(matrix[j][i] for j in range(N**2))))!=set(range(1, N**2+1)):
			out.append('No')
			done=True
			break
	if done:
		continue

	for column in range(N):
		for row in range(N):
			contents = []
			for i in range(N):
				for j in range(N):
					contents.append(matrix[N*column + i][N*row + j])
			if set(map(int, contents))!=set(range(1, N**2+1)):
				out.append('No')
				done=True
				break
		else:
			continue
		break
	else:
		out.append('Yes')

with open(argv[2], 'w') as f:
	for i in range(len(out)):
		f.write('Case #%d: %s\n'%(i+1, out[i]))
