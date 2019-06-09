from __future__ import print_function
import sys
import itertools

def solve():
    # parse input
    R, C = map(int, raw_input().split())
    cake = []
    for _ in xrange(R):
        cake.append(list(raw_input()))

    row_to_copy = -1
    copy_up = 0
    for r in xrange(R):
        last_c_hit = -1
        for c in xrange(C):
            if cake[r][c] != '?':
                if row_to_copy == -1:
                    row_to_copy = r
                if last_c_hit == -1:
                    for c2 in xrange(0, c):
                        cake[r][c2] = cake[r][c]
                else:
                    for c2 in xrange(last_c_hit + 1, c):
                        cake[r][c2] = cake[r][c]
                last_c_hit = c

        if last_c_hit == -1:
            if row_to_copy == -1:
                copy_up += 1
            else:
                cake[r] = cake[r-1][:]
        else:
            for c2 in xrange(last_c_hit + 1, C):
                cake[r][c2] = cake[r][last_c_hit]

    while copy_up > 0:
        cake[row_to_copy-1] = cake[row_to_copy][:]
        row_to_copy -= 1
        copy_up -= 1
    return '\n'.join(''.join(l) for l in cake)

T = int(raw_input())
for case in xrange(T):
    print(case, file=sys.stderr)
    print("Case #%d:\n%s"%(case+1, solve()))
