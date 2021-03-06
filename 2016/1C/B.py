#!/usr/bin/python
from __future__ import print_function
import sys
import itertools

def solve():
    # parse input
    B, M = map(int, raw_input().split())

    # solve
    if M > 2**(B - 2):
        return 'IMPOSSIBLE'
    else:
        bstring = '{0:b}'.format(M-1).rjust(B-2, '0')
        out = 'POSSIBLE\n'
        out += '0%s1\n'%(bstring[:B - 2])
        out += '\n'.join('0'*(i + 1) + '1'*(B - i - 1) for i in xrange(1, B))
        return out

T = int(raw_input())
for case in xrange(T):
    print(case, file=sys.stderr)
    print("Case #%d: %s"%(case+1, solve()))
