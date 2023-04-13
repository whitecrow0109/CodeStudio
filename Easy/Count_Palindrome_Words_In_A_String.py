from os import *
from sys import *
from collections import *
from math import *

def countNumberOfPalindromeWords(s):
    lst = s.split()
    ans = 0
    for i in range(len(lst)):
        S = lst[i].lower()
        ans += S == S[::-1]
    return ans

