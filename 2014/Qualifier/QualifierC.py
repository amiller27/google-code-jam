from sys import argv

with open(argv[1]) as f:
	data = f.read().split('\n')

out=[]
for case in range(int(data.pop(0))):
	R, C, M = map(int, data.pop(0).split())

	print case, R, C, M

	if R==1:
		out.append('c' + ('*'*M).rjust(C-1, '.'))
	elif C==1:
		out.append('\n'.join(list('c' + ('*'*M).rjust(R-1, '.'))))
	elif R*C-M==1:
		out.append('\n'.join(['*'*C for i in range(R)]))
		out[-1] = 'c' + out[-1][1:]
	elif R==2:
		if M%2 or R*C-M==2:
			out.append('Impossible')
		else:
			out.append(('*'*(M/2)).ljust(C, '.') + '\n' + ('*'*(M/2)).ljust(C-1, '.') + 'c')
	elif C==2:
		if M%2 or R*C-M==2:
			out.append('Impossible')
		else:
			out.append('**\n'*(M/2) + '..\n'*(R-M/2-1) + '.c')
	else:
		if R*C - M in [2, 3, 5, 7]:
			out.append('Impossible')
		elif (R*C - M)%2 and (R*C - M)<2*R+3:
			grid = list(list('*' for i in range(C)) for i in range(R))
			for i in range((R*C-M-3)/2):
				grid[i][0] = grid[i][1] = '.'
			for i in range(3):
				grid[i][2] = '.'
			grid[0][0] = 'c'
			out.append('\n'.join(''.join(grid[i]) for i in range(R)))
		elif (R*C - M) < 2*R:
			grid = list(list('*' for i in range(C)) for i in range(R))
			for i in range((R*C-M)/2):
				grid[i][0] = grid[i][1] = '.'
			grid[0][0] = 'c'
			out.append('\n'.join(''.join(grid[i]) for i in range(R)))
		else:
			gridString = ('*'*M).ljust(R*C, '.')
			grid = list(list(gridString[R*C-i-1::-R]) for i in range(R))
			for i in grid:print i
			if (R*C-M-1)%R==0:
				grid[1][(R*C-M-1)/R] = '.'
				grid[-1][(R*C-M-1)/R - 1] = '*'
			grid[0][0] = 'c'
			out.append('\n'.join(''.join(grid[i]) for i in range(R)))

with open(argv[2], 'w') as f:
	for i in range(len(out)):
		f.write('Case #%d:\n%s\n'%(i+1, out[i]))