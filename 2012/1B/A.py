from sys import argv
import numpy
####does not work for large input!!!!!!!

f=open(argv[1])
file_lines=f.read().split('\n')
f.close()

cases=[]
for case in range(int(file_lines.pop(0))):
    contestants=map(int,file_lines.pop(0).split(' ')[1:])
    X=sum(contestants)
    
    M=[[0 for i in range(len(contestants)+1)] for i in range(len(contestants)+1)]
    for column in range(len(M)-1):
        M[column][column]=-X
        M[column][-1]=1
    M[-1]=[1 for i in range(len(contestants))]+[0]
    M[-1][-1]=0
    M=numpy.matrix(M)
    
    B=[[contestants[i]] for i in range(len(contestants))]
    B.append([1])
    B=numpy.matrix(B)
    
    S=numpy.linalg.solve(M,B).tolist()
##    print S
    zeroes=[]
    resolve=False
    for value in range(len(S)-1):
        if S[value][0]<0:
            resolve=True
##            print 'Need to resolve case %d'%(case+1)
            zeroes.append(value)
            break
    while resolve:
##        print 'Resolving case %d'%(case+1)
        M=[[0 for i in range(len(contestants)-len(zeroes)+1)] for i in range(len(contestants)-len(zeroes)+1)]
        for column in range(len(M)-1):
            M[column][column]=-X
            M[column][-1]=1
        M[-1]=[1 for i in range(len(contestants)-len(zeroes))]+[0]
        M[-1][-1]=0
        M=numpy.matrix(M)
        
        B=[]
        for contestant in range(len(contestants)):
            if not contestant in zeroes:
                B.append([contestants[contestant]])
        B.append([1])
##        print B
        B=numpy.matrix(B)
        
##        print M
        S=numpy.linalg.solve(M,B).tolist()
        for value in zeroes:
            S.insert(value,[0])
        
        resolve=False
        for value in range(len(S)-1):
            if S[value][0]<0:
                resolve=True
##                print 'Need to resolve case %d'%(case+1)
                zeroes.append(value)
                break
    
    cases.append(map(lambda x:x[0]*100,S))
    
f=open('Google1BA.out','w')
for case in range(len(cases)):
    f.write('Case #%d: %s\n'%(case+1,' '.join(map(str,cases[case][:-1]))))
f.close()