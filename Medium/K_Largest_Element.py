from os import *
from sys import *
from collections import *
from math import *

def Klargest(a, k, n):
    a.sort()
    ans = []
    for i in range(n - k, n):
        ans.append(a[i])
    return ans