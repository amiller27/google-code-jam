from sys import argv

with open(argv[1]) as f:
	data = f.readlines()

strings = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
multiples = {2:'double', 3:'triple', 4:'quadruple', 5:'quintuple', 6:'sextuple', 7:'septuple', 8:'octuple', 9:'nonuple', 10:'decuple'}

def stringOfChunk(chunk):
	out = []

	lastDigit = chunk[0]
	count = 1

	for digit in chunk[1:] + 'E':
		if digit==lastDigit:
			count += 1
		else:
			if count == 1:
				out.append(strings[int(lastDigit)])
			elif count <= 10:
				out.extend([multiples[count], strings[int(lastDigit)]])
			else:
				out.extend(count*[strings[int(lastDigit)]])
			count = 1
		lastDigit = digit
	return ' '.join(out)

out=[]
for case in range(int(data.pop(0))):
	n, format = data.pop(0).split()

	sizes = map(int, format.split('-'))
	chunks = []
	for i in range(len(sizes)):
		chunks.append(n[:sizes[i]])
		n = n[sizes[i]:]

	out.append(' '.join(map(stringOfChunk, chunks)))

with open(argv[2], 'w') as f:
	for i in range(len(out)):
		f.write('Case #%d: %s\n'%(i+1, out[i]))
