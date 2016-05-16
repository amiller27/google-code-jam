from sys import argv
import itertools

with open(argv[1]) as f:
	data = f.read().split('\n')

def has(l, item):
	for i in l:
		if i[0]==item[0] and i[1]==item[1]:
			return True
	return False

out=[]
for case in range(int(data.pop(0))):
	N, M = map(int, data.pop(0).split())
	cities = list(str(data.pop(0)) for i in range(N))
	flights = map(lambda x:[x[0]-1, x[1]-1], [map(int, data.pop(0).split()) for i in range(M)])

	currentMin = 'A'
	for com in itertools.permutations(range(N), N):
		current = cities[com[0]]
		currentCity = com[0]
		for i in range(1, len(com)):
			print current, currentCity
			if has(flights, [currentCity, com[i]]):
				current +=(cities[com[i]])
				currentCity = com[i]
				continue
			for city in com[:i]:
				if has(flights, [city, com[i]]):
					current += (cities[com[i]])
					currentCity = com[i]
					break
			else:
				break
		if current < currentMin and len(current) == 5*N:
			currentMin = current
	out.append(currentMin)
			



with open(argv[2], 'w') as f:
	for i in range(len(out)):
		f.write('Case #%d: %s\n'%(i+1, out[i]))