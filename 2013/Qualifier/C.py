from sys import argv
from math import sqrt, ceil, floor
import decimal
decimal.getcontext().prec = 100

f=open(argv[1])
txt=f.readlines()
f.close()
				
def permutations(ones, length):
	p=[['']]
	for i in range(length):
		p.append([])
		for s in p[-2]:
			p[-1].append(s+'0')
			if s.count('1')<ones:
				p[-1].append(s+'1')
	return p[-1]

out = []
for case in range(int(txt.pop(0))):
	a, b = txt.pop(0).split(' ')
	
	sqrta = str(decimal.Decimal(a).sqrt().to_integral_value(rounding='ROUND_CEILING'))
	sqrtb = str(decimal.Decimal(b).sqrt().to_integral_value(rounding='ROUND_FLOOR'))
	
	c = 0
		
	startmag = len(sqrta)
	if (sqrta.lstrip('2')>'2' and len(sqrta)>1) or (len(sqrta)==1 and int(sqrta)>3):
		startmag+=1
		sqrta='1' + '0'*len(sqrta)
	
	if int(sqrta)>int(sqrtb):
		out.append(0)
		print case+1, '\r',
		continue
	
	endmag = len(sqrtb)
	if startmag==endmag:
		if startmag==1:
			if int(sqrta)<=1<=int(sqrtb):
				c+=1
		elif startmag==2:
			if int(sqrta)<=11<=int(sqrtb):
				c+=1
		elif startmag==3:
			if int(sqrta)<=101<=int(sqrtb):
				c+=1
			if int(sqrta)<=111<=int(sqrtb):
				c+=1
		else:
			for n in permutations(3 if startmag>=8 else (startmag-2)/2, (startmag-2)/2):
				if int(sqrta)<=int('1' + ''.join(n) + '0'*(1 if startmag%2 else 0) + ''.join(n)[::-1] + '1')<=int(sqrtb):
					c+=1
				if startmag%2 and int(sqrta)<=int('1' + ''.join(n) + '1' + ''.join(n)[::-1] + '1')<=int(sqrtb):
					c+=1
		
		if startmag==1:
			if int(sqrta)<=2<=int(sqrtb):
				c+=1
		elif startmag==3:
			if int(sqrta)<=121<=int(sqrtb):
				c+=1
		elif startmag>=5 and startmag%2:
			for n in permutations(1, (startmag-3)/2):
				if int(sqrta)<=int('1' + n + '2' + n[::-1] + '1')<=int(sqrtb):
					c+=1
		
		if startmag>1:
			##more than one digit
			if int(sqrta)<=int('2' + '0'*(startmag-2) + '2')<=int(sqrtb):
				c+=1
			if startmag%2 and int(sqrta)<=int('2' + '0'*((startmag-3)/2) + '1' + '0'*((startmag-3)/2) + '2')<=int(sqrtb):
				c+=1
		
		if int(sqrta)<=3<=int(sqrtb) and startmag==1:
			c+=1
			
	else:
		for currentmag in [startmag, endmag]:
			if currentmag==1:
				if int(sqrta)<=1<=int(sqrtb):
					c+=1
			elif currentmag==2:
				if int(sqrta)<=11<=int(sqrtb):
					c+=1
			elif currentmag==3:
				if int(sqrta)<=101<=int(sqrtb):
					c+=1
				if int(sqrta)<=111<=int(sqrtb):
					c+=1
			else:
				for n in permutations(3 if currentmag>=8 else (currentmag-2)/2, (currentmag-2)/2):
					if int(sqrta)<=int('1' + ''.join(n) + '0'*(1 if currentmag%2 else 0) + ''.join(n)[::-1] + '1')<=int(sqrtb):
						c+=1
					if currentmag%2 and int(sqrta)<=int('1' + ''.join(n) + '1' + ''.join(n)[::-1] + '1')<=int(sqrtb):
						c+=1
			
			if currentmag==1:
				if int(sqrta)<=2<=int(sqrtb):
					c+=1
			elif currentmag==3:
				if int(sqrta)<=121<=int(sqrtb):
					c+=1
			elif currentmag>=5 and currentmag%2:
				for n in permutations(1, (currentmag-3)/2):
					if int(sqrta)<=int('1' + n + '2' + n[::-1] + '1')<=int(sqrtb):
						c+=1
			
			if currentmag>1:
				##more than one digit
				if int(sqrta)<=int('2' + '0'*(currentmag-2) + '2')<=int(sqrtb):
					c+=1
				if currentmag%2 and int(sqrta)<=int('2' + '0'*((currentmag-3)/2) + '1' + '0'*((currentmag-3)/2) + '2')<=int(sqrtb):
					c+=1
			
			if int(sqrta)<=3<=int(sqrtb) and currentmag==1:
				c+=1

		
		
		for currentmag in range(startmag+1, endmag):
			#middle range
			#case 1
			if currentmag>2:
				n = (currentmag-2)/2
				c+= (1 + n + n*(n-1)/2 + n*(n-1)*(n-2)/6) * (2 if currentmag%2 else 1)
			else:
				c+=1
			#case 2
			if currentmag%2:
				if currentmag==1:
					c+=1
				else:
					c+=1
					c+=(currentmag-3)/2
				
			#case 3
			if currentmag>=2:
				c+=1
				if currentmag%2:
					c+=1
			#case 4
			if currentmag==1:
				c+=1
		
	out.append(c)
	print case+1, '\r',
	
outfile = open(argv[2], 'w')
for i in range(len(out)):
	outfile.write('Case #%i: %s\n'%(i+1, out[i]))
outfile.close()