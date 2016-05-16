from sys import argv

with open(argv[1]) as f:
	data = f.read().split('\n')

out=[]
for case in xrange(int(data.pop(0))):
	# raw_input()

	N = int(data.pop(0))
	colors = []
	for i in xrange(N):
		colors.append(data.pop(0))

	M = int(data.pop(0))
	lifts = []
	for i in xrange(M):
		lifts.append(map(int, data.pop(0).split()))

	S = int(data.pop(0))
	soldiers = []
	for i in xrange(S):
		soldiers.append(map(int, data.pop(0).split()))

	colorCount = len(set(colors))

	colorlifts = []
	times = []
	for lift in lifts:
		if colors[lift[0]-1]==colors[lift[1]-1]:
			# print 'useless lift'
			continue
		if [colors[lift[0]-1], colors[lift[1]-1]] in colorlifts:
			if times[colorlifts.index([colors[lift[0]-1], colors[lift[1]-1]])] > lift[2]:
				times[colorlifts.index([colors[lift[0]-1], colors[lift[1]-1]])] = lift[2]
			# print 'duplicate lift'
			continue
		colorlifts.append([colors[lift[0]-1], colors[lift[1]-1]])
		times.append(lift[2])

	out.append([])

	print ''
	print N
	print colors
	assert len(colors)==N
	print M
	print lifts
	assert len(lifts)==M
	print S
	print soldiers
	assert len(soldiers)==S
	print colorCount
	print colorlifts
	print times
	print len(colorlifts)
	assert len(colorlifts) == len(times)

	for start, destination in soldiers:

		startcolor = colors[start-1]
		endcolor = colors[destination-1]

		if startcolor == endcolor:
			out[-1].append('0')
			continue

		liftsleft = colorlifts[:]
		timesleft = times[:]

		feedercolors = []
		feedertimes = []

		for l in xrange(len(colorlifts)):
			if colorlifts[l][1]==endcolor:
				feedercolors.append(colorlifts[l][0])
				feedertimes.append(times[l])

				i = liftsleft.index(colorlifts[l])
				del liftsleft[i]
				del timesleft[i]

		addedSomething = True
		while addedSomething:
			l=0
			addedSomething = False
			
			while l < len(liftsleft):
				if liftsleft[l][1] in feedercolors:
					if liftsleft[l][0] in feedercolors:
						if feedertimes[feedercolors.index(liftsleft[l][0])] > feedertimes[feedercolors.index(liftsleft[l][1])] + timesleft[l]:
							feedertimes[feedercolors.index(liftsleft[l][0])] = feedertimes[feedercolors.index(liftsleft[l][1])] + timesleft[l]
					else:
						feedercolors.append(liftsleft[l][0])
						feedertimes.append(feedertimes[feedercolors.index(liftsleft[l][1])] + timesleft[l])
						addedSomething = True
					del liftsleft[l]
					del timesleft[l]
					continue
				else:
					l+=1

		if startcolor in feedercolors:
			out[-1].append(str(feedertimes[feedercolors.index(startcolor)]))
		else:
			out[-1].append('-1')

with open(argv[2], 'w') as f:
	for i in range(len(out)):
		f.write('Case #%d: \n%s\n'%(i+1, '\n'.join(out[i])))