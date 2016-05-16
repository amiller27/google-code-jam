from sys import argv
from math import floor, sqrt
import decimal
decimal.getcontext().prec = 100

f=open(argv[1])
txt=f.readlines()
f.close()

out=[]
for case in range(int(txt.pop(0))):
	r, t = map(int, txt.pop(0).split(' '))
	
	r = decimal.Decimal(r)
	t = decimal.Decimal(t)
	print r, t
	
	n = ((1-2*r+((2*r-1)**2+8*t).sqrt())/decimal.Decimal(4)).to_integral_value(rounding='ROUND_FLOOR')
	out.append(n)
	
outfile = open(argv[2], 'w')
for i in range(len(out)):
	outfile.write('Case #%i: %s\n'%(i+1, out[i]))
outfile.close()