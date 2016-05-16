from sys import argv

f=open(argv[1])
file_lines=f.read().split('\n')
f.close()

cases=[]
for case in range(int(file_lines.pop(0))):
    contestants=map(int,file_lines.pop(0).split(' ')[1:])
    X=sum(contestants)
    
    K=2.0*X/len(contestants)
    S=map(lambda Ji:(K-Ji)/X,contestants)
    
##    print S
    zeroes=[]
    resolve=False
    for value in range(len(S)):
        if S[value]<0:
            resolve=True
##            print 'Need to resolve case %d'%(case+1)
            zeroes.append(value)
            break
    while resolve:
##        print 'Resolving case %d'%(case+1)
        nonzeroes=contestants[:]
        zeroes.sort(reverse=True)
        for contestant in zeroes:
            del nonzeroes[contestant]
        zeroes.sort()
        
        print S,zeroes,nonzeroes
        K=float(sum(nonzeroes)+X)/len(nonzeroes)
        S=map(lambda Ji:(K-Ji)/X,nonzeroes)
        for value in zeroes:
            S.insert(value,0)
##        print S
        
        resolve=False
        for value in range(len(S)):
            if S[value]<0:
                resolve=True
##                print 'Need to resolve case %d'%(case+1)
                zeroes.append(value)
                break
    
    cases.append(map(lambda x:x*100,S))
    
f=open('Google1BA.out','w')
for case in range(len(cases)):
    f.write('Case #%d: %s\n'%(case+1,' '.join(map(str,cases[case]))))
f.close()