from sys import argv
from decimal import *

with open(argv[1]) as f:
	data = f.read().split('\n')

out=[]
for case in range(int(data.pop(0))):
	print case
	C, F, X = map(Decimal, data.pop(0).split())

	elapsedTime = Decimal(0)
	I = Decimal(2.0)
	while (X-C)/I > X/(I+F):
		elapsedTime += C/I
		I += F

	elapsedTime += X/I

	out.append(elapsedTime)


with open(argv[2], 'w') as f:
	for i in range(len(out)):
		f.write('Case #%d: %s\n'%(i+1, out[i]))