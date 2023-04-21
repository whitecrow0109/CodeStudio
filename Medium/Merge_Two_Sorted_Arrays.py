from math import *
from collections import *
from sys import *
from os import *

def ninjaAndSortedArrays(arr1,arr2,m,n):
    lst = []
    for i in range(m):
        lst.append(arr1[i])
    for i in range(n):
        lst.append(arr2[i])
    lst.sort()
    return lst
