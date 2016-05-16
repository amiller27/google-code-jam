from sys import argv

##unpacks data from file
f=open(argv[1])
file_lines=f.read().split('\n')
f.close()

cases=[]
for case in range(int(file_lines.pop(0))):
    lanes={'L':set(),'R':set()}
    for car in range(int(file_lines.pop(0))):
        car=file_lines.pop(0).split(' ')
        lanes[car[0]].add(car[1:])
    print lanes