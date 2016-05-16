from sys import argv

with open(argv[1]) as f:
	data = f.read().split('\n')

out=[]
for case in xrange(int(data.pop(0))):
	N = int(data.pop(0))
	maze = []

	for i in range(N):
		maze.append(data.pop(0))

	sx, sy, ex, ey = map(lambda s:int(s)-1, data.pop(0).split())

	print N, sx, sy
	for s in maze: print s

	## FIND START DIRECTION
	if (sx==0 or maze[sx-1][sy]=='#'):
		hdirection = 0
	elif (sy==N-1 or maze[sx][sy+1]=='#'):
		hdirection = 1
	elif (sx==N-1 or maze[sx+1][sy]=='#'):
		hdirection = 2
	elif (sy==0 or maze[sx][sy-1]=='#'):
		hdirection = 3
	else:
		raise Exception('NO WALLS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

	x=(hdirection+1)%4
	for i in range(4):
		if x==0 and sx!=0 and maze[sx-1][sy]!='#':
			break
		if x==1 and sy!=N-1 and maze[sx][sy+1]!='#':
			break
		if x==2 and sx!=N-1 and maze[sx+1][sy]!='#':
			break
		if x==3 and sy!=0 and maze[sx][sy-1]!='#':
			break

		if i==3:
			out.append('Edison ran out of energy.')

		hdirection = x
		x = (x+1)%4
	else:
		continue

	moves=''
	## MAKE MOVES
	position = [sx, sy]
	for step in xrange(10000):

		if position[0] == ex and position[1] == ey:
			break

		if ((hdirection==0 and (position[0]==0 or maze[position[0]-1][position[1]]=='#'))
			or (hdirection==1 and (position[1]==N-1 or maze[position[0]][position[1]+1]=='#'))
			or (hdirection==2 and (position[0]==N-1 or maze[position[0]+1][position[1]]=='#'))
			or (hdirection==3 and (position[1]==0 or maze[position[0]][position[1]-1]=='#'))):

			while ((hdirection==3 and (position[0]==0 or maze[position[0]-1][position[1]]=='#'))
				or (hdirection==0 and (position[1]==N-1 or maze[position[0]][position[1]+1]=='#'))
				or (hdirection==1 and (position[0]==N-1 or maze[position[0]+1][position[1]]=='#'))
				or (hdirection==2 and (position[1]==0 or maze[position[0]][position[1]-1]=='#'))):

				hdirection = (hdirection+1)%4

			if hdirection==0:
				position[1]+=1
				moves += 'E'
			elif hdirection==1:
				position[0]+=1
				moves += 'S'
			elif hdirection==2:
				position[1]-=1
				moves += 'W'
			elif hdirection==3:	
				position[0]-=1
				moves += 'N'
		
		elif hdirection==0 and position[0]!=0 and maze[position[0]-1][position[1]]!='#':
			position[0]-=1
			moves += 'N'
			hdirection = 3

		elif hdirection==1 and position[1]!=N-1 and maze[position[0]][position[1]+1]!='#':
			position[1]+=1
			moves += 'E'
			hdirection = 0
			
		elif hdirection==2 and position[0]!=N-1 and maze[position[0]+1][position[1]]!='#':
			position[0]+=1
			moves += 'S'
			hdirection = 1

		elif hdirection==3 and position[1]!=0 and maze[position[0]][position[1]-1]!='#':
			position[1]-=1
			moves += 'W'
			hdirection = 2
		else:
			raise Exception('FAIL!!!!!!!')
	else:
		if position[0] != ex or position[1] != ey:
			out.append('Edison ran out of energy.')
			continue

	out.append(str(step) + '\n' + moves)


with open(argv[2], 'w') as f:
	for i in range(len(out)):
		f.write('Case #%d: %s\n'%(i+1, out[i]))
