#!/usr/bin/python
from __future__ import print_function
import sys
import itertools

def solve():
    # parse input
    B, M = map(int, raw_input().split())

    # solve
    if M > 2**(B-2):
        return 'IMPOSSIBLE'
    else:
        out = 'POSSIBLE\n'
        bstring = '{0:b}'.format(M-1).rjust(B-2, '0')
        out += '0'
        for i in xrange(B-2):
            if bstring[i] == '1':
                out += '1'
            else:
                out += '0'
        out += '1\n'

        for i in xrange(1, B):
            out += ''.join('0' if j <= i else '1' for j in xrange(B))
            out += '\n'
        return out[:-1]

T = int(raw_input())
for case in xrange(T):
    print(case, file=sys.stderr)
    print("Case #%d: %s"%(case+1, solve()))
