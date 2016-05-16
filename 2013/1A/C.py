from sys import argv
import random

f = open(argv[1])
txt = f.readlines()
f.close()

out = []
T = int(txt.pop(0))
R, N, M, K = map(int, txt.pop(0).split())
rand = random.Random()

def factors(n):
	factor_list = []
	for i in range(2, M+1):
		while n%i==0:
			n/=i
			factor_list.append(i)
	return factor_list
	
def combine(l):
	factor_list = l[0][:]
	for new_list in l[1:]:
		for i in range(2, M+1):
			if factor_list.count(i) < new_list.count(i):
				factor_list.extend([i]*(new_list.count(i)-factor_list.count(i)))
	return factor_list
	

def list_works(l, new_n):
	if new_n==4:
		l.remove(2)
		l.remove(2)
		l.append(4)
	elif new_n==6:
		l.remove(2)
		l.remove(3)
		l.append(6)
	elif new_n==8:
		l.remove(2)
		l.remove(4)
		l.append(8)
	elif new_n==28:
		l.remove(4)
		l.remove(4)
		l.append(2)
		l.append(8)
	elif new_n==44:
		l.remove(2)
		l.remove(8)
		l.append(4)
		l.append(4)
	elif new_n==34:
		l.remove(2)
		l.remove(6)
		l.append(3)
		l.append(4)
	elif new_n==26:
		l.remove(3)
		l.remove(4)
		l.append(2)
		l.append(6)
	else:
		raise ValueError
	
	for factor_list in product_factors:
		needed3 = factor_list.count(3)
		needed6 = needed3 - (l.count(3) if l.count(3)<needed3 else needed3)
		needed2 = factor_list.count(2) - needed6
		
		result = False
		for eights in range(needed2/3 if needed2/3<l.count(8) else l.count(8), -1, -1):
			result = True
			if needed2/3:
				needed2 -= eights*3
			if needed2/2:
				needed2 -= needed2/2*2 if needed2/2*2<l.count(4)*2 else l.count(4)*2
			if needed2 > l.count(2) + (needed3-needed6 if needed3-needed6 < l.count(6)-needed6 else l.count(6)-needed6):
				result = False
			
			if result == True:
				break
		if result == False:
			return False
	return True
	


for case in range(R):
	print case+1
	products = map(int, txt.pop(0).split())
	# print products, 'p'
	product_factors = map(factors, products)
	# for i in product_factors:print i, 'f'
	
	prime_list = combine(product_factors)
	final_list = prime_list[:]
	# print final_list, 'l'
	
	added2=0
	added3=0
	i=0
	ceiling=(prime_list.count(2)+prime_list.count(3))**3
	if case==7298:
		print products
		for l in product_factors:print l
		print prime_list
		ceiling*=10
		
	six1st = True
	while len(final_list) > N:
		i+=1
		if i>ceiling:
			six1st = not six1st
		if i>2*ceiling:
			if added2+added3 > 5:
				final_list = final_list[:N]
				break
			six1st = not six1st
			print 'adding 1'
			final_list = prime_list[:]
			if added2==11:
				added2=0
				added3+=1
			else:
				added2+=1
			final_list.extend([2]*added2)
			final_list.extend([3]*added3)
			i=0
		# if final_list.count(2) >= 1 and final_list.count(3) >= 1 and list_works(final_list[:], 6) and six1st:
			# final_list.remove(2)
			# final_list.remove(3)
			# final_list.append(6)
		if final_list.count(2) >= 2 and list_works(final_list[:], 4):
			final_list.remove(2)
			final_list.remove(2)
			final_list.append(4)
		elif final_list.count(2) >= 1 and final_list.count(4) >= 1 and list_works(final_list[:], 8):
			final_list.remove(2)
			final_list.remove(4)
			final_list.append(8)
		elif final_list.count(2) >= 1 and final_list.count(3) >= 1 and list_works(final_list[:], 6):
			final_list.remove(2)
			final_list.remove(3)
			final_list.append(6)
		elif final_list.count(4) >= 2 and list_works(final_list[:], 28):
			final_list.remove(4)
			final_list.remove(4)
			final_list.append(2)
			final_list.append(8)
		elif final_list.count(2) >= 1 and final_list.count(8) >= 1 and list_works(final_list[:], 44):
			final_list.remove(2)
			final_list.remove(8)
			final_list.append(4)
			final_list.append(4)
		elif final_list.count(3) >= 1 and final_list.count(4) >= 1 and list_works(final_list[:], 26):
			final_list.remove(3)
			final_list.remove(4)
			final_list.append(2)
			final_list.append(6)
		elif final_list.count(6) >= 1 and final_list.count(2) >= 1 and list_works(final_list[:], 34):
			final_list.remove(6)
			final_list.remove(2)
			final_list.append(3)
			final_list.append(4)
		else:
			print 'no options, adding 1'
			final_list = prime_list[:]
			if added2==11:
				added2=0
				added3+=1
			else:
				added2+=1
			final_list.extend([2]*added2)
			final_list.extend([3]*added3)
			i=0
		
	while len(final_list) < N:
		final_list.append(rand.choice(range(2, M+1)))
		
	out.append(''.join(map(str, final_list)))

outfile = open(argv[2], 'w')
outfile.write('Case #1:\n')
for i in range(len(out)):
	outfile.write('%s\n'%(out[i]))
outfile.close()