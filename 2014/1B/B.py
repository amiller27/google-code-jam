from sys import argv

with open(argv[1]) as f:
	data = f.read().split('\n')

out=[]
for case in range(int(data.pop(0))):
	A, B, K = map(int, data.pop(0).split())

	if K>=A or K>=B:
		out.append(A*B)
	else:
		out.append(K*A + K*B - K*K)
		# add numbers for a and b > K

with open(argv[2], 'w') as f:
	for i in range(len(out)):
		f.write('Case #%d: %s\n'%(i+1, out[i]))