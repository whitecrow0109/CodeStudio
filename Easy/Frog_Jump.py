from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:
    MX, N = 1000000005, 100005
    ans = [MX] * N
    ans[0] = 0
    for i in range(1, n):
        ans[i] = min(ans[i], ans[i - 1] + abs(heights[i] - heights[i - 1]))
        if i >= 2:
            ans[i] = min(ans[i], ans[i - 2] + abs(heights[i] - heights[i - 2]))
    return ans[n - 1]
