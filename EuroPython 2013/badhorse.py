from sys import argv
import itertools

f = open(argv[1])
data = f.readlines()
f.close()

def addMember(member):
	if member in teams[0] or member in teams[1] or member is None:
		return True

	enemies = []
	for pair in pairs:
		if member == pair[0]:
			enemies.append(pair[1])
			if pair[1] in members:
				members.remove(pair[1])
		elif member == pair[1]:
			enemies.append(pair[0])
			if pair[0] in members:
				members.remove(pair[0])

	if not filter(lambda enemy : enemy in teams[0], enemies):
		teams[0].add(member)
	elif not filter(lambda enemy : enemy in teams[1], enemies):
		teams[1].add(member)
	else: 
		return False

	if list(itertools.ifilterfalse(addMember, enemies)):
		return False
	return True


out=[]
for case in range(int(data.pop(0))):
	M = int(data.pop(0))
	pairs = list(data.pop(0).split() for i in range(M))
	members = list(set(sum(pairs, [])))

	out.append('Yes')

	teams = [set(), set()]
	while len(members):
		if not addMember(members.pop()):
			out[-1] = 'No'
			break

f = open(argv[2], 'w')
for i in range(len(out)):
	f.write('Case #%d: %s\n'%(i+1, out[i]))
f.close()
