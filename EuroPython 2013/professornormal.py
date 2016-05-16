from sys import argv
import numpy, math

f = open(argv[1])
data = f.readlines()
f.close()

def calculateTransitions(board):
	transitions = list(list(0 for i in range(N)) for i in range(M))
	for i in range(M):
		for j in range(N):
			if board[i, j] != 0:
				transitions[i][j] -= 12
				receivers = []
				if j>0 and board[i, j-1] != 0:
					receivers.append([i, j-1])
				if i>0 and board[i-1, j] != 0:
					receivers.append([i-1, j])
				if j<N-1 and board[i, j+1] != 0:
					receivers.append([i, j+1])
				if i<M-1 and board[i+1, j] != 0:
					receivers.append([i+1, j])

				for kid in receivers:
					transitions[kid[0]][kid[1]] += 12/len(receivers)

	return numpy.matrix(transitions)

def calculateTurns(board, transitions):
	currentMin = 10**12
	for i in range(M):
		for j in range(N):
			if transitions[i, j]>=0:
				continue
			turns = int(math.ceil(float(11 - board[i, j])/transitions[i, j]))
			if turns < currentMin:
				currentMin = turns
	return currentMin

out = []
for case in range(int(data.pop(0))):
	M = int(data.pop(0))
	N = int(data.pop(0))
	children = numpy.matrix(list(map(int, data.pop(0).split()) for i in range(M)))

	print case
	print M, N
	print sum(children)
	out.append([0, 'turns'])
	while 1:

		for i in range(M):
			for j in range(N):
				if children[i,j] < 12:
					children[i,j] = 0
					continue

				if j>0 and children[i, j-1] >= 12:
					continue
				if i>0 and children[i-1, j] >= 12:
					continue
				if j<N-1 and children[i, j+1] >= 12:
					continue
				if i<M-1 and children[i+1, j] >= 12:
					continue

				children[i, j] = 0

		transitions = calculateTransitions(children)

		kidsLeft = 0
		for i in range(M):
			for j in range(N):
				if children[i, j] != 0:
					kidsLeft += 1
		if kidsLeft == 0:
			break

		stable = True
		for i in range(M):
			for j in range(N):
				if transitions[i,j] != 0:
					stable = False
					break
			else:
				continue
			break
		if stable:
			out[-1] = [kidsLeft, 'children will play forever']
			break

		turnsTilChange = calculateTurns(children, transitions)

		children += turnsTilChange * transitions
		out[-1][0] += turnsTilChange

f = open(argv[2], 'w')
for i in range(len(out)):
	f.write('Case #%d: %s\n'%(i+1, ' '.join(map(str, out[i]))))
f.close()