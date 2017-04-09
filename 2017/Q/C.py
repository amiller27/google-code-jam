from __future__ import print_function
import sys
import itertools

def solve():
    # parse input
    N, K = map(int, raw_input().split())

    # solve
    n1 = N
    n2 = N+1
    nn1 = 1
    nn2 = 0

    while True:
        print(n1, n2, nn1, nn2, K, file=sys.stderr)
        if K <= nn2:
            return n2/2, (n2-1)/2
        elif K <= nn1 + nn2:
            return n1/2, (n1-1)/2
        else:
            K -= nn1 + nn2
            new_nn1 = 0
            new_nn2 = 0
            new_n1 = (n1-1)/2
            new_n2 = n2/2
            if n1 % 2:
                new_nn1 += 2*nn1
            else:
                new_nn1 += nn1
                new_nn2 += nn1
            if n2 % 2:
                new_nn2 += 2*nn2
            else:
                new_nn1 += nn2
                new_nn2 += nn2

            n1 = new_n1
            n2 = new_n2
            nn1 = new_nn1
            nn2 = new_nn2

T = int(raw_input())
for case in xrange(T):
    print(case, file=sys.stderr)
    print("Case #%d: %s"%(case+1, ' '.join(map(str, solve()))))
