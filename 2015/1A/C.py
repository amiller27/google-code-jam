from __future__ import print_function
import sys
import itertools

def bound(points):
	print("entering bound", file=sys.stderr)
	boundary = []
	leftx = min(i[0] for i in points)
	leftminy = min(i[1] for i in filter(lambda x: x[0]==leftx, points))
	for p in points:
		if p[0]==leftx:
			boundary.append(p)
	p.sort()

	rightx = max(i[0] for i in points)
	while boundary[-1][0] != rightx:
		print(points, file=sys.stderr)
		print(boundary, file=sys.stderr)
		slope = float("-inf")
		point_to_add = None
		for point in points:
			if point in boundary:
				continue
			print(point, file=sys.stderr)
			# if point[0] == boundary[-1][0]:
			# 	print("breaking", file=sys.stderr)
			# 	boundary.append(point)
			# 	point_to_add = None
			# 	break
			if point[0] > boundary[-1][0]:
				newslope = float(point[1] - boundary[-1][1])/(point[0] - boundary[-1][0])
				if newslope > slope or (abs(newslope-slope)<0.0000000001 and point[0]<point_to_add[0]):
					slope = newslope
					point_to_add = point
		if point_to_add!=None:
			boundary.append(point_to_add)

	addition = list(reversed(sorted(filter(lambda x:x[0]==rightx, points))))
	boundary.extend(addition[1:])
	while boundary[-1][0] != boundary[0][0]:
		print(points, file=sys.stderr)
		print(boundary, file=sys.stderr)
		slope = float("-inf")
		point_to_add = None
		for point in points:
			if point in boundary[1:]:
				continue
			if point[0] == boundary[-1][0]:
				boundary.append(point)
				break
			if point[0] < boundary[-1][0]:
				newslope = float(point[1] - boundary[-1][1])/(point[0] - boundary[-1][0])
				if newslope > slope or (abs(newslope-slope)<0.0000000001 and point[0]>point_to_add[0]):
					slope = newslope
					point_to_add = point
		if point_to_add!=None:
			boundary.append(point_to_add)

	if boundary[0]==boundary[-1]:
		boundary.pop()
	print("exiting bound", file=sys.stderr)
	return boundary




def solve():
	# parse input
	N = int(raw_input())
	coords = list(map(int, raw_input().split()) for i in range(N))

	# solve
	out = []
	if N<4:
		return "\n0"*N
	boundary = bound(coords)
	for point in range(len(coords)):
		points_mpoint = coords[:point] + coords[point+1:]
		for remaining in range(N, 3, -1):
			for comb in itertools.combinations(points_mpoint, remaining-1):
				print(coords[point], file=sys.stderr)
				print(list(comb) + [coords[point]], file=sys.stderr)
				print(bound(list(comb) + [coords[point]]), file=sys.stderr)

				if coords[point] in bound(list(comb) + [coords[point]]):
					print(N, remaining, file=sys.stderr)
					out.append(N-remaining)
					break
			if len(out)==point+1:
				break
		if len(out)<point+1:
			out.append(N-3)
	return "\n" + "\n".join(map(str, out))



T = int(raw_input())
for case in xrange(T):
	print(case, file=sys.stderr)
	print("Case #%d:%s"%(case+1, solve()))
