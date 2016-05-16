from sys import argv
from math import log

with open(argv[1]) as f:
	data = f.readlines()

def pos(p, q):
	if p==q:
		return 1, 1
	if p<q:
		parentPos = pos(p, q-p)
		return parentPos[0]+1, 2*parentPos[1]-1
	else:
		parentPos = pos(p-q, q)
		return parentPos[0]+1, 2*parentPos[1]

def pq(row, column):
	if row==1:
		return 1, 1
	if column%2:
		parent = pq(row-1, (column-1)/2 + 1)
		return parent[0], sum(parent)
	else:
		parent = pq(row-1, column/2)
		return sum(parent), parent[1]

out = []
for case in range(int(data.pop(0))):
	if data[0][0]=='1':
		[F, N] = map(int, data.pop(0).split())
		row = int(log(N, 2)) + 1
		column = N - 2**(row-1) + 1
		out.append(' '.join(map(str, pq(row, column))))
	else:
		[F, P, Q] = map(int, data.pop(0).split())
		row, column = pos(P, Q)
		out.append(2**(row-1) - 1 + column)

with open(argv[2], 'w') as f:
	for i in range(len(out)):
		f.write('Case #%d: %s\n'%(i+1, out[i]))