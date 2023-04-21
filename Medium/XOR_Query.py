from os import *
from sys import *
from collections import *
from math import *

def xorQuery(queries):
    lst, now = [], 0
    for i in range(len(queries) - 1, -1, -1):
        if (queries[i][0] == 1):
            lst.append(queries[i][1] ^ now)
        else:
            now ^= queries[i][1]
    lst.reverse()
    return lst