from __future__ import print_function
import sys
import itertools

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpha = map(str.upper, alpha)

def solve():
    # parse input
    N = int(raw_input())
    P = map(int, raw_input().split())
    pairs = map(list, enumerate(P))
    total = sum(p[1] for p in pairs)
    result = []

    # solve
    while len(pairs) > 1:
        pairs.sort(key = lambda p: p[1])
        if pairs[-2][1] <= float(total - 1) / 2:
            #remove one from top
            result.append(alpha[pairs[-1][0]])
            pairs[-1][1] -= 1
            if pairs[-1][1] == 0: del pairs[-1]
            total -= 1
        else:
            #remove from top two
            result.append(alpha[pairs[-1][0]] + alpha[pairs[-2][0]])
            pairs[-1][1] -= 1
            pairs[-2][1] -= 1
            if pairs[-2][1] == 0: del pairs[-2]
            if pairs[-1][1] == 0: del pairs[-1]
            total -= 2
        #if len(pairs) > 2 and pairs[-3][1] == pairs[-2][1] == pairs[-1][1] == 1:
        #    # remove one from top
        #    result.append(alpha[pairs[-1][0]])
        #    del pairs[-1]
        #    total -= 1
        #if pairs[-2][1] > float(total - 2)/2 or pairs[-1][1] < 2:
        #    # remove from top two
        #    result.append(alpha[pairs[-1][0]] + alpha[pairs[-2][0]])
        #    pairs[-2][1] -= 1
        #    pairs[-1][1] -= 1
        #    if pairs[-2][1] == 0:
        #        del pairs[-2]
        #    if pairs[-1][1] == 0:
        #        del pairs[-1]
        #    total -= 2
        #else:
        #    # remove from top
        #    result.append(2 * alpha[pairs[-1][0]])
        #    pairs[-1][1] -= 2
        #    if pairs[-1][1] == 0:
        #        del pairs[-1]
        #    total -= 2
    if len(pairs):
        result.extend(pairs[0][1] * alpha[pairs[0][0]])
    return ' '.join(result)

T = int(raw_input())
for case in xrange(T):
    print(case, file=sys.stderr)
    print("Case #%d: %s"%(case+1, solve()))
