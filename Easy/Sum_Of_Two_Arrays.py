from os import *
from sys import *
from collections import *
from math import *

def findArraySum(a, n, b, m):
    A, B = 0, 0
    for i in range(n):
        A = A * 10 + a[i]
    for i in range(m):
        B = B * 10 + b[i]
    C = A + B
    lst = []
    while C:
        lst.append(C % 10)
        C //= 10
    lst.reverse()
    return " ".join(str(x) for x in lst)