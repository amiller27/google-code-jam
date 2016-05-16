from sys import argv

##reads input file
f=open(argv[1])
file_lines=f.read().split('\n')
f.close()

for case in range(int(file_lines.pop(0))):#one iteration per room setup
    h,w,d=map(int,file_lines.pop(0).split(' '))
    
    verticals=[set() for n in range(w-1)]#list of sets of vertical lines
    horizontals=[set([0,h-2]) for n in range(w-2)]#list of sets of horizontal lines
    
    verticals[0]=set(range(h-2))#adds vertical left border
    verticals[-1]=set(range(h-2))#adds vertical right border
    
    file_lines.pop(0)#removes opening line of pounds
    
    for line in range(h-2):#number of interior rows
        for column in range(1,w-1):#number of interior squares
            
            if file_lines[0][column]=='#':
                verticals[column-1].add(line)
                verticals[column].add(line)
                horizontals[column-1].add(line)
                horizontals[column-1].add(line+1)
            elif file_lines[0][column+1]=='X':
                x=(column+0.5,line+0.5)
        file_lines.pop(0)
    
    file_lines.pop(0)#removes ending line of pounds
    
    print horizontals
    print verticals







##printed the grid and x-location
    for row in range(h-2):
        
        print '',
        for column in range(w-2):
            if row in horizontals[column]:print '-',
            else:print ' ',
        print ''
        
        for column in range(w-1):
            if row in verticals[column]:print 'I',
            else:print ' ',
        print ''
        
    print '',
    for column in range(w-2):
        if h-2 in horizontals[column]:print '-',
        else:print ' ',
    print '\nX at %r\n'%list(x)


def intersects(lr,m,x1,y1,horiz,vert,h,w):
    get_y=lambda x:m*(x-x1)+y1
    get_x=lambda y:(y-y1)/m+x1
    if lr=='r':
        from math import floor,ceil,sqrt
        
        for column in range(x1.ceil(),w-1):
            if get_y(column).floor() in vert[column]:
                out=(column,get_y(column))
                break
            
        for row in range(y1.ceil(),h-1):
            if row in horiz[get_x(row).floor()]:
                try:out
                except UnboundLocalError or NameError:return #the horizontal hit
                
                d=lambda x1,y1,x2,y2:sqrt((x1+x2)**2+(y1+y2)**2)
                
                if d(x1,y1,get_x(row),row) < d(x1,y1,out[0],out[1]):
                    return #the horizontal hit
                elif d(x1,y1,get_x(row),row) > d(x1,y1,out[0],out[1]):
                    return #the vertical hit
                else:#it hit a corner!!!!!!!
                    pass
