from sys import argv

f = open(argv[1])
lines = f.readlines()
f.close()

out = []
for case in range(int(lines.pop(0))):
	out.append(0)
	n = int(lines.pop(0))
	names = list(lines.pop(0) for i in range(n))
	last = names[0]
	for name in names:
		if name<last:
			out[case] += 1
		else:	
			last = name

f = open(argv[2], 'w')
for i in range(len(out)):
	f.write('Case #%d: %d\n'%(i+1, out[i]))
f.close()