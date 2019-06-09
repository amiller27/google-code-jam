from __future__ import print_function
from __future__ import division
import sys
import math
import itertools

cache = {}
def rsolve(Q, used):
    if used in cache:
        return cache[used]

    max_t = 0
    for comb in itertools.product(*[range(len(Q[i])) for i in range(len(Q))]):
        allowed_quantity = []
        for i, j in enumerate(comb):
            if used[i][j]:
                break
            if not allowed_quantity:
                allowed_quantity = [int(math.ceil(Q[i][j]*10/11)), int(Q[i][j]*10/9)]
                if allowed_quantity[0] > allowed_quantity[1]:
                    break
            else:
                if int(math.ceil(Q[i][j]*10/11)) > allowed_quantity[1]:
                    break
                if int(Q[i][j]*10/9) < allowed_quantity[0]:
                    break
                allowed_quantity = [max(int(math.ceil(Q[i][j]*10/11)), allowed_quantity[0]), min(int(Q[i][j]*10/9), allowed_quantity[1])]
        else:
            used_c = tuple((used[ii] if ii != i else tuple((used[ii][jj] if jj != j else True) for jj in xrange(len(used[0])))) for ii in xrange(len(used)))
            result = rsolve(Q, used_c)
            max_t = max(max_t, result + 1)
    cache[used] = max_t
    return max_t


def solve():
    # parse input
    N, P = map(int, raw_input().split())
    R = map(int, raw_input().split())
    Q = ([([int(i) for i in raw_input().split()]) for _ in xrange(N)])
    print(Q, file=sys.stderr)
    for i in range(len(Q)):
        for j in range(len(Q[i])):
            Q[i][j] /= R[i]

    Q = [list(reversed(sorted(Q[i]))) for i in range(len(Q))]
    print(N, P, file=sys.stderr)

    matches = 0
    while True:
        print('q1', Q, file=sys.stderr)
        for i in range(len(Q)):
            while Q[i] and (Q[i][-1] < 1 or Q[i][-1]/math.floor(Q[i][-1]) > 11/10) and Q[i][-1]/math.ceil(Q[i][-1]) < 9/10:
                Q[i].pop()
        print('q2', Q, file=sys.stderr)
        if [True for l in Q if not l]:
            return matches
        mint = float('Inf')
        mini = -1
        for i in range(len(Q)):
            if Q[i][-1] < mint:
                mint = Q[i][-1]
                mini = i
        assert mint != float('Inf')
        assert mini >= 0
        print(mint, mini, file=sys.stderr)

        overlap = [10/11*Q[0][-1], 10/9*Q[0][-1]]
        if overlap[0] > overlap[1]:
            Q[mini].pop()
        else:
            for i in range(1, len(Q)):
                overlap = [max(overlap[0], 10/11*Q[i][-1]), min(overlap[1], 10/9*Q[i][-1])]
                if overlap[0] > overlap[1]:
                    break
            else:
                for i in range(len(Q)):
                    Q[i].pop()
                matches += 1
                continue
            Q[mini].pop()

    #result = rsolve(Q, tuple(tuple(False for j in xrange(len(Q[i]))) for i in xrange(len(Q))))
    #global cache
    #cache = {}
    #return result

T = int(raw_input())
for case in xrange(T):
    print(case, file=sys.stderr)
    print("Case #%d: %s"%(case+1, solve()))
