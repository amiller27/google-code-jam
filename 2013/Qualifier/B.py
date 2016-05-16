from sys import argv

f=open(argv[1])
txt=f.readlines()
f.close()

out = []
for case in range(int(txt.pop(0))):
	n, m = map(int, txt.pop(0).split(' '))
	lawn = [map(int, txt.pop(0).split(' ')) for i in range(n)]
	
	for row in range(n):
		for column in range(m):
			if len(out)==case and len(filter(lambda x : x>lawn[row][column], lawn[row])) and len(filter(lambda x : x>lawn[row][column], [lawn[i][column] for i in range(n)])):
				out.append('NO')
	
	if len(out)==case:
		out.append('YES')
		
outfile = open(argv[2], 'w')
for i in range(len(out)):
	outfile.write('Case #%i: %s\n'%(i+1, out[i]))
outfile.close()