from sys import argv

with open(argv[1]) as f:
	data = f.read().split('\n')

out=[]
for case in range(int(data.pop(0))):
	A, B, K = map(int, data.pop(0).split())
	count=0
	for i in range(A):
		for j in range(B):
			if i&j < K:
				count += 1
	out.append(count)


with open(argv[2], 'w') as f:
	for i in range(len(out)):
		f.write('Case #%d: %s\n'%(i+1, out[i]))