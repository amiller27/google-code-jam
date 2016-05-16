def recycled_nums(n):
    list_n=str(n)
    
    out=set()
    for i in list_n[1:]:
        list_n=list_n[1:]+list_n[0]
        next=int(''.join(list_n))
        
        if next>n:
            out.add(next)
    return out


from sys import argv

f=open(argv[1])
lines=f.read().split('\n')
f.close()

out=[]
for i in range(int(lines.pop(0))):
    start,end=map(int,lines[i].split(' '))
    
    pairs=0
    
    for n in range(start,end+1):
        
        for num in recycled_nums(n):
            
            if num<=end:
                pairs+=1

    out.append('Case #%i: %i'%(i+1,pairs))
    print out[-1]
    

f=open('GoogleQCOut.txt','w')
f.write('\n'.join(out))
f.close()