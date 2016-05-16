def normal_score(x):
    if not x%3:
        return x/3
    return x/3+1


def surprising_score(x):
    if x%3==2:
        return x/3+2
    elif x==0:
        return 0
    return x/3+1


from sys import argv

f=open(argv[1])
lines=f.read().split('\n')
f.close()


out=[]

for i in range(int(lines.pop(0))):
    line=map(int,lines[i].split(' '))
    n=line.pop(0)
    surprising=line.pop(0)
    best=line.pop(0)
    
    winners=0
    for googler in line:
        if normal_score(googler)>=best:
            winners+=1
            
        elif normal_score(googler)==best-1:
            if surprising>0:
                if surprising_score(googler)==best:
                    surprising-=1
                    winners+=1
                    
    out.append('Case #%i: %i'%(i+1,winners))
    print out[-1]
    
    
f=open('GoogleQBOut.txt','w')
f.write('\n'.join(out))
f.close()