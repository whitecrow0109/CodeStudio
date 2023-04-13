from typing import *
import bisect

def binarySearch(arr : List[int], n : int, x : int) :
    idx = bisect.bisect_left(arr, x, 0, n)
    if idx < 0 or idx >= n:
        return -1
    return idx
