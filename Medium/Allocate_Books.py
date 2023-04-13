from os import *
from sys import *
from collections import *
from math import *

def ayushGivesNinjatest(n, m, time):
    def can(p):
        cur, cnt = 0, 0
        for i in range(m):
            if time[i] > p: return 0
            cur += time[i]
            if cur > p:
                cnt += 1
                cur = time[i]
        return cnt + 1 <= n

    lo, hi = 1, 10000000000000
    while lo + 1 < hi:
        mid = lo + hi >> 1
        if can(mid): hi = mid
        else: lo = mid
    return lo if can(lo) else hi