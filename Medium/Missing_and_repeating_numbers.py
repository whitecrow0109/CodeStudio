from math import *
from collections import *
from sys import *
from os import *

N = 50005

def missingAndRepeating(arr, n):
    cnt = [0] * N
    for i in range(n):
        cnt[arr[i]] += 1
    M, R = -1, -1
    for i in range(1, n + 1):
        if cnt[i] == 0:
            M = i
        if cnt[i] == 2:
            R = i
    return M, R
