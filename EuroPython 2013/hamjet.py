import sys, math, decimal
with open(sys.argv[1]) as f: data = list(map(decimal.Decimal, i) for i in map(str.split, f.readlines()))
with open(sys.argv[2], 'w') as f: f.write('\n'.join('Case #%d: %f'%(i, math.asin(decimal.Decimal(9.8)*data[i][1]/data[i][0]**2)*90/math.pi) for i in range(1, int(data[0][0])+1)))
