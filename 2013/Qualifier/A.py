from sys import argv

f=open(argv[1])
txt=f.readlines()
f.close()


out=[]
for case in range(int(txt.pop(0))):
	board = []
	for i in range(4):
		board.append(txt.pop(0))
	txt.pop(0)
		
	for line in board:
		if line.count('X')==3 and line.count('T')==1:
			out.append('X won')
			break
		elif line.count('O')==3 and line.count('T')==1:
			out.append('O won')
			break
		elif line.count('X')==4:
			out.append('X won')
			break
		elif line.count('O')==4:
			out.append('O won')
			break
			
	if len(out)==case:
		for index in range(4):
			line = ''.join([board[0][index], board[1][index], board[2][index], board[3][index]])
			
			if line.count('X')==3 and line.count('T')==1:
				out.append('X won')
				break
			elif line.count('O')==3 and line.count('T')==1:
				out.append('O won')
				break
			elif line.count('X')==4:
				out.append('X won')
				break
			elif line.count('O')==4:
				out.append('O won')
				break

	if len(out)==case:
		line = ''.join([board[0][0], board [1][1], board[2][2], board[3][3]])
		if line.count('X')==3 and line.count('T')==1:
			out.append('X won')
		elif line.count('O')==3 and line.count('T')==1:
			out.append('O won')
		elif line.count('X')==4:
			out.append('X won')
		elif line.count('O')==4:
			out.append('O won')
		
	if len(out)==case:
		line = ''.join([board[0][3], board[1][2], board[2][1], board[3][0]])
		if line.count('X')==3 and line.count('T')==1:
			out.append('X won')
		elif line.count('O')==3 and line.count('T')==1:
			out.append('O won')
		elif line.count('X')==4:
			out.append('X won')
		elif line.count('O')==4:
			out.append('O won')

	if len(out)==case:
		dots = sum([s.count('.') for s in board])
		print dots
		if dots:
			out.append('Game has not completed')
		else:
			out.append('Draw')
			
outfile=open(argv[2], 'w')
for line in range(len(out)):
	outfile.write('Case #%d: %s\n'%(line+1, out[line]))
outfile.close()