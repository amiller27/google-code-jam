from __future__ import print_function
import sys
import itertools
import math
import sys
sys.setrecursionlimit(100000)

def opt(cakes, i, k, cache=None):
    if cache is None:
        cache = {}
    if (i, k) in cache:
        return cache[(i, k)]

    if k == 0:
        cache[(i, k)] = 0
    elif i == len(cakes):
        cache[(i, k)] = -float('Inf')
    else:
        cache[(i, k)] = max(opt(cakes, i+1, k-1, cache)
                               + 2*math.pi*cakes[i][0]*cakes[i][1]
                               + (math.pi*cakes[i][0]**2 if k == 1 else 0),
                            opt(cakes, i+1, k, cache))
    return cache[(i, k)]

def solve():
    # parse input
    N, K = map(int, raw_input().split())
    cakes = [map(int, raw_input().split()) for _ in range(N)]
    cakes = sorted(cakes, key=lambda cake: cake[0])
    print(cakes, K, file=sys.stderr)
    return opt(cakes, 0, K)

T = int(raw_input())
for case in xrange(T):
    print(case, file=sys.stderr)
    print("Case #%d: %s"%(case+1, solve()))
