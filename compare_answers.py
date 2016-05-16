from sys import argv

with open(argv[1]) as f:
	s1 = f.readlines()
with open(argv[2]) as f:
	s2 = f.readlines()

for i in range(len(s1)):
	if s1[i]!=s2[i]:
		print i, s1[i], s2[i]