from sys import argv

f=open(argv[1])
file_lines=f.read().split('\n')
f.close()

cases=[]
for case in range(int(file_lines.pop(0))):
    waterh,maph,mapw=map(int,file_lines.pop(0).split(' '))
    ceilings=[map(int,file_lines.pop(0).split(' ')) for i in range(maph)]
    floors=[map(int,file_lines.pop(0).split(' ')) for i in range(maph)]
    
    print waterh
    print maph,mapw
    print ceilings
    print floors