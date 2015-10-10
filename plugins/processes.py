#!/usr/bin/python

import psutil
ps = []


def processes():
    global ps
    if not ps:
        ps = map(lambda o: psutil.Process(o).name(), psutil.pids())
        if not ps:
            return "Empty"

        # remove duplicates and sort
        ps = sorted(list(set(ps)))
        ps.reverse()

    p = ps.pop()
    return p
