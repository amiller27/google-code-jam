from __future__ import print_function
import sys
import itertools

def solve():
    # parse input
    S, k = raw_input().split()
    S = list(S)
    k = int(k)

    # solve
    flips = 0
    for s in range(len(S) - k + 1):
        if S[s] == '-':
            flips += 1
            for s2 in range(k):
                S[s+s2] = '-' if (S[s+s2]=='+') else '+'
    if '-' in S:
        return 'IMPOSSIBLE'
    else:
        return flips

T = int(raw_input())
for case in xrange(T):
    print(case, file=sys.stderr)
    print("Case #%d: %s"%(case+1, solve()))
