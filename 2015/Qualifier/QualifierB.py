from __future__ import print_function
import sys

solved = {}

def solve(diners):
	# print(diners, file=sys.stderr)
	hstring = " ".join(map(str, diners))
	if hstring in solved:
		return solved[hstring]
	if max(diners) == 1:
		solved[hstring] = 1
		return 1
	moves = []
	# print(filter(None, map(lambda x:x-1, diners)))
	moves.append(solve(filter(None, map(lambda x:x-1, diners))))
	for i in range(1, diners[-1]):
		moves.append(solve(sorted(diners[:-1] + [diners[-1]-i, i])))

	solved[hstring] = min(moves) + 1
	return min(moves) + 1

N = int(raw_input())

for case in xrange(N):
	print(case, file=sys.stderr)
	D = int(raw_input())
	diners = sorted(map(int, raw_input().split()))
	print("Case #%d: %d"%(case+1, solve(diners)))
