from sys import argv

try:
    f=open(argv[1])
    lines=f.read().split('\n')
    f.close()
except:pass

e_to_g={
    'a':'y',
    'b':'n',
    'c':'f',
    'd':'i',
    'e':'c',
    'f':'w',
    'g':'l',
    'h':'b',
    'i':'k',
    'j':'u',
    'k':'o',
    'l':'m',
    'm':'x',
    'n':'s',
    'o':'e',
    'p':'v',
    'q':'z',
    'r':'p',
    's':'d',
    't':'r',
    'u':'j',
    'v':'g',
    'w':'t',
    'x':'h',
    'y':'a',
    'z':'q',
    ' ':' '}

g_to_e=dict([(e_to_g[i],i) for i in e_to_g])

out=list(['' for i in range(int(lines.pop(0)))])

for i in range(len(out)):
    for char in lines[i]:
        out[i]+=g_to_e[char]
    print out[i]
    
f=open('GoogleQAsOut.txt', 'w')
s=[]
for i in range(len(out)):
    s.append('Case #%i: %s'%(i+1,out[i]))
f.write('\n'.join(s))
f.close()