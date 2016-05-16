from sys import argv
import math
from decimal import Decimal

f = open(argv[1])
txt = f.readlines()
f.close()

out = []
for case in range(int(txt.pop(0))):
	print case+1
	N, X, Y = map(int, txt.pop(0).split())
	# print N, X, Y
	
	if X>0:
		yint = X+Y
	elif X<0:
		yint = Y-X
	elif X==0:
		yint = Y
	else:
		raise ValueError
		
	L = yint/2
	# print 'L =', L
	
	Av = N + L - 2*L**2
	# print 'Av =', Av
	
	if Av >= 2*L + Y + 1:
		out.append(1.0)
	elif Av < Y + 1:
		out.append(0.0)
	elif X==0 and Av < 4*L + 1:
		out.append(0.0)
	else:
		m = min(2*L, Av)
		# print 'm =', m
		numerator = sum([Decimal(math.factorial(Av))/math.factorial(Av-i)/math.factorial(i) for i in range(Y+1, m+1)], Decimal(0))
		denominator = sum([Decimal(math.factorial(Av))/math.factorial(Av-i)/math.factorial(i) for i in range(max(0, Av-2*L), m+1)], Decimal(0))
		# print numerator
		# print denominator
		out.append(numerator/denominator)
	
	assert 0<=out[-1]<=1
	# print out[-1]
	# raw_input()
out_file = open(argv[2], 'w')
for i in range(len(out)):
	out_file.write('Case #%d: %f\n'%(i+1, out[i]))
out_file.close()