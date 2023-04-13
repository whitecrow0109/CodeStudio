from os import *
from sys import *
from collections import *
from math import *

def getInversions(arr, n):
    nxt, idx = arr.copy(), {}
    nxt.sort()
    n = len(nxt)
    for i in range(n):
        idx[nxt[i]] = i + 1
    cnt = [0] * (n + 5)

    def insert(val):
        while val <= n:
            cnt[val] += 1
            val += val & -val
    
    def query(val):
        ans = 0
        while val >= 1:
            ans += cnt[val]
            val -= val & -val
        return ans

    ret = 0
    for i in range(n - 1, -1, -1):
        ret += query(idx[arr[i]])
        val = idx[arr[i]]
        insert(val)
    return ret

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))