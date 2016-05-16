from sys import argv

##reads input file
f=open(argv[1])
file_lines=f.read().split('\n')
f.close()

def beaten_all(levels):
    for level in levels:
        if level[1]!='x':
            return False
    return True

cases=[]
for case in range(int(file_lines.pop(0))):
    levels=[map(int,file_lines.pop(0).split(' ')) for i in range(int(file_lines.pop(0)))]
    points=0
    for attempt in range(len(levels)*2):
        beat_lvl=False
        for level in levels:#tests lvl2 possibilities for 2 pts
            if level[1]!='x' and level[1]<=points and level[0]!='x':
                points+=2
                level[0]='x'
                level[1]='x'
                beat_lvl=True
                break
        if not beat_lvl:
            for level in levels:#tests lvl2 possibilities for 1pt
                if level[1]!='x' and level[1]<=points:
                    points+=1
                    level[1]='x'
                    beat_lvl=True
                    break
            if not beat_lvl:
                max=[1001,-1]
                for level in levels:#tests lvl1 possibilities
                    if level[0]!='x' and level[0]<=points:
                        if level[1]>max[1]:
                            max=[levels.index(level),level[1]]
                if max[0]<1001:
                    points+=1
                    levels[max[0]][0]='x'
                    beat_lvl=True
                if not beat_lvl:
                    attempt='Too Bad'
                    break
        if beaten_all(levels):
            attempt+=1
            break
    cases.append(attempt)

f=open('Google1AB.out','w')
for case in range(len(cases)):
    f.write('Case #%d: %s\n'%(case+1,cases[case]))
f.close()
