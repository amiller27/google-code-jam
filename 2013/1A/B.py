from sys import argv

f=open(argv[1])
txt=f.readlines()
f.close()

def first_half(values, start, end):
	# print values, start, end, 'first'
	if len(values)==0:
		# print 0
		return 0
	elif len(values)==1:
		if end-R <= start:
			# print values[0] * (start-(end-R))
			return values[0] * (start-(end-R))
		else:raise
	else:
		max_index = values.index(max(values))
		E_at_max = start + R*max_index
		if E_at_max>E:
			E_at_max=E
		E_spent = E_at_max - end + (len(values)-max_index)*R
		if E_spent>E_at_max:
			E_spent=E_at_max
		# print first_half(values[:max_index], start, E_at_max) + E_spent*values[max_index] + second_half(values[max_index+1:], E_at_max-E_spent+R, end)
		return first_half(values[:max_index], start, E_at_max) + E_spent*values[max_index] + second_half(values[max_index+1:], E_at_max-E_spent+R, end)
	
def second_half(values, start, end):
	# print values, start, end, 'second'
	if len(values)==0:
		# print 0
		return 0
	elif len(values)==1:
		if end-R <= start:
			# print values[0] * (start-(end-R))
			return values[0] * (start-(end-R))
		else:raise
	else:
		max_index = values.index(max(values))
		E_at_max = start + R*max_index
		if E_at_max>E:
			E_at_max=E
		E_spent = E_at_max - end + (len(values)-max_index)*R
		if E_spent>E_at_max:
			E_spent=E_at_max
		# print first_half(values[:max_index], start, E_at_max) + E_spent*values[max_index] + second_half(values[max_index+1:], E_at_max-E_spent+R, end)
		return first_half(values[:max_index], start, E_at_max) + E_spent*values[max_index] + second_half(values[max_index+1:], E_at_max-E_spent+R, end)
	

out = []
for case in range(int(txt.pop(0))):
	# raw_input()
	# print case, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
	E, R, N = map(int, txt.pop(0).split())
	values = map(int, txt.pop(0).split())
	
	if N!=len(values):raise
	
	if R>=E:
		out.append(E*sum(values))
	elif N==1:
		out.append(values[0]*E)
	elif R<E:
		out.append(first_half(values[:values.index(max(values))], E, E) + E*values[values.index(max(values))] + second_half(values[values.index(max(values))+1:], R, R))
	
outfile = open(argv[2], 'w')
for i in range(len(out)):
	outfile.write('Case #%i: %s\n'%(i+1, out[i]))
outfile.close()