from sys import argv

f=open(argv[1])
txt=f.readlines()
f.close()

out = []
for case in range(int(txt.pop(0))):
	k, n = map(int, txt.pop(0).split(' '))
	skeys = map(int, txt.pop(0).split(' '))
	chests = list([map(int, txt.pop(0).split(' ')) for i in range(n)])
	
	
	keys = skeys[:]
	order = [0]*n
	i = 0
	
	print chests
	print order
	print n
	while 1:
		print order
		if chests[order[i]][0] in keys and (not order[i] in order[:i]):
			if i==n-1:
				out.append(' '.join([str(k+1) for k in order]))
				break
			keys.remove(chests[order[i]][0])
			keys.extend(chests[order[i]][2:])
			i+=1
		else:
			if sum([1 if (not x in order[:i] and chests[x][0] in keys) else 0 for x in range(order[i]+1, n)]):
				for x in range(order[i]+1, n):
					if not x in order[:i] and chests[x][0] in keys:
						order[i]=x
						break
			else:
				done=False
				while not sum([1 if (not x in order[:i] and chests[x][0] in keys) else 0 for x in range(order[i]+1, n)]) and not done:
					order[i]=0
					i-=1
					if i==-1:
						break
					keys.append(chests[order[i]][0])
					for key in chests[order[i]][2:]:
						keys.remove(key)
					for x in range(order[i]+1, n):
						if not x in order[:i] and chests[x][0] in keys:
							order[i]=x
							done=True
							break
		if i==-1:
			out.append('IMPOSSIBLE')
			break
	print out[-1]
outfile = open(argv[2], 'w')
for i in range(len(out)):
	outfile.write('Case #%i: %s\n'%(i+1, out[i]))
outfile.close()