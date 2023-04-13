from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def uniqueSubsets(n :int,arr :List[int]) -> List[List[int]]:
    x = sorted(arr)
    ans, S = [], []
    for i in range(1, (1 << n)):
        now = []
        for j in range(n):
            if (i & 1 << j):
                now.append(x[j])
        S.append(now)
    S.sort()
    ans.append(S[0])
    for i in range(1, (1 << n) - 1):
        if S[i] != S[i - 1]:
            ans.append(S[i])
    return ans
