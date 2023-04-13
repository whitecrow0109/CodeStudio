from typing import *

N = 1000005

def pickCoupons(n: int, coupons: List[int]) -> int:
    ans = N
    x = {}
    for i in range(n):
        idx = coupons[i]
        if idx in x.keys():
            ans = min(ans, i - x[idx] + 1)
        x[idx] = i
    if ans == N: ans = -1
    return ans
