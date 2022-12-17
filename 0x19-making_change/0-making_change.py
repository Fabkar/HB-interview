#!/usr/bin/python3
""" module doc """


def makeChange(cs, ttl):
    """
    function doc
    """
    if ttl <= 0:
        return 0
    cs.sort(reverse=True)
    s = 0
    i = 0
    ct = 0
    n_c = len(cs)
    while s < ttl and i < n_c:
        while cs[i] <= ttl - s:
            s += cs[i]
            ct += 1
            if s == ttl:
                return ct
        i += 1
    return -1
    