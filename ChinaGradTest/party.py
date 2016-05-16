from sys import argv

with open(argv[1]) as f:
	data = f.read().split('\n')

out=[]
for case in range(int(data.pop(0))):
	print '\n\n'
	print case
	B = int(data.pop(0))
	rects = list(map(int, data.pop(0).split()) for i in range(B))
	print B

	people = []
	for rect in rects:
		for i in range(rect[0], rect[2]+1):
			for j in range(rect[1], rect[3]+1):
				people.append([i, j])
	
	totalpeople = len(people)
	print totalpeople

	xlist = sorted(i[0] for i in people)
	ylist = sorted(i[1] for i in people)

	xreversed = list(reversed(xlist[:]))
	yreversed = list(reversed(ylist[:]))

	closest = [people[0]]
	print closest
	for person in people[1:]:
		if case==5:
			print person
			print xlist.index(person[0])
			print xreversed.index(person[0])
			print ylist.index(person[1])
			print yreversed.index(person[1])
		if abs(xlist.index(person[0]) - xreversed.index(person[0])) + abs(ylist.index(person[1]) - yreversed.index(person[1])) < abs(xlist.index(closest[0][0]) - xreversed.index(closest[0][0])) + abs(ylist.index(closest[0][1]) - yreversed.index(closest[0][1])):
			closest = [person]
			print closest
		elif abs(xlist.index(person[0]) - xreversed.index(person[0])) + abs(ylist.index(person[1]) - yreversed.index(person[1])) == abs(xlist.index(closest[0][0]) - xreversed.index(closest[0][0])) + abs(ylist.index(closest[0][1]) - yreversed.index(closest[0][1])): 
			closest.append(person)
			print closest

	closest = sorted(closest)[0]
	print closest

	d=0
	for person in people:
		d+= abs(person[0]-closest[0]) + abs(person[1]-closest[1])

	out.append('%d %d %d'%(closest[0], closest[1], d))

with open(argv[2], 'w') as f:
	for i in range(len(out)):
		f.write('Case #%d: %s\n'%(i+1, out[i]))
