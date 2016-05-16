from sys import argv

with open(argv[1]) as f:
	data = f.read()

depth = 0
chunksToRemove = []
i=0
while 1:
	if i>len(data):
		break
	if data[i:i+2]=='/*':
		if depth == 0:
			chunksToRemove.append([i])
		depth+=1
		i+=1
	elif data[i:i+2]=='*/' and depth>0:
		if depth == 1:
			chunksToRemove[-1].append(i+2)
		depth-=1
		i+=1
	i+=1

for chunk in chunksToRemove[::-1]:
	data = data[:chunk[0]] + data[chunk[1]:]

with open(argv[2], 'w') as f:
	f.write('Case #1:\n' + data)