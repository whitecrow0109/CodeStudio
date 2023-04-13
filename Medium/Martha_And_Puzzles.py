from os import *
from sys import *
from collections import *
from math import *

def harderPuzzle(n, puzzle):
    MX = 100005
    idx = [MX] * 105
    ans = []
    for i in range(n - 1, -1, -1):
        pos = MX
        for j in range(puzzle[i] + 1, 101):
            pos = min(pos, idx[j])
        if pos == MX:
            ans.append(0)
        else:
            ans.append(abs(pos - i))
        idx[puzzle[i]] = min(idx[puzzle[i]], i)
    ans.reverse()
    return ans