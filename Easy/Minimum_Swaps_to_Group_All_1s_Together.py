from os import *
from sys import *
from collections import *
from math import *

def groupAllOneTogether(arr, n):
    zero, one, num = 0, 0, [0]
    for i in range(n):
        if arr[i] == 1:
            one += 1
        else:
            zero += 1
        num.append(zero)
    if one == 0:
        return -1
    ans = 5005
    for i in range(n - one + 1):
        ans = min(ans, num[i + one] - num[i])
    return ans