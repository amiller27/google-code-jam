from __future__ import print_function
import sys
import itertools

def solve():
	# parse input
	N = int(raw_input())
	parents = []
	for i in xrange(N):
		parents.append(map(lambda x:int(x)-1, raw_input().split()[1:]))

	# solve
	parentscombined = sum(parents, [])
	tops = filter(lambda x: parentscombined.count(x)>1, set(parentscombined))
	# bottoms = filter(lambda x: len(parents[x])>1, xrange(N))

	# print(parents, file=sys.stderr)

	if len(parentscombined)==0:
		return "No"

	for curr_root in range(N):
		roots = parents[curr_root][:]
		if len(roots)==0 or curr_root in parentscombined:
			continue
		
		traversed_nodes = set(range(curr_root+1) + filter(lambda x: len(parents[x])==0, range(curr_root+1, N)))
		for i in range(2000):
			# print("roots: ", roots, file=sys.stderr)
			# print("traversed: ", traversed_nodes, file=sys.stderr)
			if len(set(roots)) != len(roots):
				return "Yes"
			if sum(len(parents[x]) for x in roots) == 0:
				break
			newroots = []
			for root in roots:
				traversed_nodes.add(root)
				if len(parents[root])>0:
					newroots.extend(parents[root])
				else:
					newroots.append(root)
			roots = newroots
	return "No"

T = int(raw_input())

for case in xrange(T):
	print(case, file=sys.stderr)
	print("Case #%d: %s"%(case+1, solve()))
