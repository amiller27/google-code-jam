from sys import argv

def max2(l):
	l=list(l)
	top = max(l[:2])
	next = min(l[:2])
	for n in l[2:]:
		if n>top:
			next=top
			top=n
		elif n>next:
			next = n
	return top+next

def maxTreeSize(root, parent, tree):
	# print '\nmaxTreeSize'
	# print root
	# print parent
	# print tree
	children = []
	for pair in tree:
		if root in pair and parent not in pair:
			children.append(pair[0] if pair[1]==root else pair[1])
	# print children
	if len(children) in [0, 1]:
		# print 'returning 1'
		# raw_input()
		return 1
	if len(children)==2:
		# print 'returning', maxTreeSize(root=children[0], parent=root, tree=pairs), maxTreeSize(root=children[1], parent=root, tree=pairs)
		# raw_input()
		return 1 + maxTreeSize(root=children[0], parent=root, tree=pairs) + maxTreeSize(root=children[1], parent=root, tree=pairs)
	# print 'returning', max2(maxTreeSize(root=i, parent=root, tree=pairs) for i in children)
	# raw_input()
	return 1 + max2(maxTreeSize(root=i, parent=root, tree=pairs) for i in children)


with open(argv[1]) as f:
	data = f.read().split('\n')

out=[]
for case in range(int(data.pop(0))):
	# print ''
	print case
	N = int(data.pop(0))
	pairs = list([map(int, data.pop(0).split()) for i in range(N-1)])

	# print pairs

	maxSize = 1
	for root in range(1, N+1):
		# print root
		count = 0
		children = []
		for pair in pairs:
			if root in pair:
				count+=1
				children.append(pair[0] if root==pair[1] else pair[1])
		# print count
		# print children
		if count == 1:
			continue
		elif count == 2:
			maxSize = max(1 + maxTreeSize(root=children[0], parent=root, tree=pairs) + maxTreeSize(root=children[1], parent=root, tree=pairs), maxSize)
		else:
			maxSize = max(1 + max2(maxTreeSize(root=i, parent=root, tree=pairs) for i in children), maxSize)
	out.append(N-maxSize)


with open(argv[2], 'w') as f:
	for i in range(len(out)):
		f.write('Case #%d: %s\n'%(i+1, out[i]))