from sys import argv

f = open(argv[1])
txt = f.readlines()
f.close()

def solve_case(A, N, motes):
	print 'A =', A
	print 'N =', N
	print 'motes =', motes
	if A==1:
		return N
	
	count = [0]*N
	for i in range(len(motes)):
		if motes[i]<A:
			print A, motes[i], 'all good'
			A+=motes[i]
			print A, motes[i], 'added'
		else:
			print 'not good'
			while A<=motes[i]:
				print 'still not good', A, motes[i]
				if count[i] == N-i:
					return sum(count)
				A = 2*A-1
				count[i] +=1
			print A, motes[i], 'now we\'re good'
			A+=motes[i]
			print A, motes[i], 'added'
	print min(sum(count), N)
	# raw_input()
	return min(sum(count), N)

out = []
for case in range(int(txt.pop(0))):
	A, N = map(int, txt.pop(0).split())
	motes = sorted(map(int, txt.pop(0).split()))
	
	out.append(solve_case(A, N, motes))
	
	
out_file = open(argv[2], 'w')
for i in range(len(out)):
	out_file.write('Case #%d: %d\n'%(i+1, out[i]))
out_file.close()