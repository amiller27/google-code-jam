from sys import argv
import decimal

##computes product of list items
def product(l):
    p=decimal.Decimal(1.0)
    for i in l:
        p*=decimal.Decimal(i)
    return p

##reads input, saves as file_lines
f=open(argv[1])
file_lines=f.read().split('\n')
f.close()


case_values=[]
for case in range(int(file_lines.pop(0))):#one test case per iteration
    
    ##unpacks all data
    chars_typed,chars_total=map(int,file_lines.pop(0).split(' '))
    probs=map(float,file_lines.pop(0).split(' '))
    
    ##computes initial values
    min=chars_total+2#total if press enter immediately
    prob_right=product(probs)
    K=2*chars_total-chars_typed+2
    
    ##total if continue typing
    keys = K-prob_right*(chars_total+1)#(chars_total-chars_typed+1)*prob_right+(2*chars_total-chars_typed+2)*(1-prob_right)    
    if keys<min:min=keys
    
    for n_of_bspaces in range(1,chars_typed):
        prob_right/=decimal.Decimal(probs[-n_of_bspaces])
        keys = 2*n_of_bspaces+K-prob_right*(chars_total+1)#(2*n_of_bspaces+chars_total-chars_typed+1)*prob_right+(2*n_of_bspaces+2*chars_total-chars_typed+2)*(1-prob_right)
        if keys<min:min=keys
        
    case_values.append(min)
    
    print chars_typed
    print chars_total
    print ''
    if case==14:print probs
    print '%d\r'%case,
print case_values

##writes final data to file
f=open('Google1AA.out','w')
for case in range(len(case_values)):
    f.write('Case #%i: %f\n'%(case+1,case_values[case]))
f.close()
