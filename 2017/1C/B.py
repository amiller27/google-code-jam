from __future__ import print_function
import sys
import itertools

def solve():
    # parse input
    Ac, Aj = map(int, raw_input().split())
    Tc = [['c'] + map(int, raw_input().split()) for _ in range(Ac)]
    Tj = [['j'] + map(int, raw_input().split()) for _ in range(Aj)]

    tasks = sorted(Tc + Tj, key=lambda task: task[1])
    c_time = sum((task[2] - task[1]) for task in Tj)
    j_time = sum((task[2] - task[1]) for task in Tc)

    free_time = 0
    req_switches = 0
    cur_p = tasks[0][0]
    last_t = tasks[0]
    ints_taken_by_c = []
    ints_taken_by_j = []
    for task in tasks[1:]:
        p, c, d = task
        if p != cur_p:
            req_switches += 1
            free_time += c - last_t[2]
            cur_p = p
        else:
            if p == 'c':
                if c - last_t[2] > 0:
                    ints_taken_by_j.append(c - last_t[2])
            else:
                if c - last_t[2] > 0:
                    ints_taken_by_c.append(c - last_t[2])
        last_t = task
    p, c, d = tasks[0]
    if p != cur_p:
        req_switches += 1
        free_time += c - last_t[2] + 1440
    else:
        if p == 'c':
            if c - last_t[2] + 1440 > 0:
                ints_taken_by_j.append(c - last_t[2] + 1440)
        else:
            if c - last_t[2] + 1440 > 0:
                ints_taken_by_c.append(c - last_t[2] + 1440)

    print(tasks, c_time, j_time, file=sys.stderr)
    print(free_time, req_switches, ints_taken_by_c, ints_taken_by_j, file=sys.stderr)

    ints_taken_by_c.sort()
    ints_taken_by_j.sort()

    while 1440 - min(c_time+sum(ints_taken_by_c), 720) - min(j_time+sum(ints_taken_by_j), 720) > free_time:
        if not ints_taken_by_c:
            free_time += ints_taken_by_j.pop()
        elif not ints_taken_by_j:
            free_time += ints_taken_by_c.pop()
        elif ints_taken_by_c[-1] > ints_taken_by_j[-1]:
            free_time += ints_taken_by_c.pop()
        else:
            free_time += ints_taken_by_j.pop()
        req_switches += 2
    return req_switches

T = int(raw_input())
for case in xrange(T):
    print(case, file=sys.stderr)
    print("Case #%d: %s"%(case+1, solve()))
