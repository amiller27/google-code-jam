from sys import argv

f=open(argv[1])
file_lines=f.read().split('\n')
f.close()

cases=[]
for case in range(int(file_lines.pop(0))):
    n,m=map(int,file_lines.pop(0).split(' '))
    paths=[file_lines.pop(0) for i in range(n)]
    count=0
    for newpath in range(m):
        newpathlist=file_lines.pop(0)[1:].split('/')
        
        i=1
        while not (('/'+('/'.join(newpathlist))) in paths):
            if not '/'+('/'.join(newpathlist[:i])) in paths:
                paths.append('/'+('/'.join(newpathlist[:i])))
                count+=1
            i+=1
    cases.append(count)

f=open('GoogleFileFixIt.out','w')
f.write('\n'.join(['Case #%i: %i'%(case+1,cases[case]) for case in range(len(cases))]))
f.close()