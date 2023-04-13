from os import *
from sys import *
from collections import *
from math import *

def firstMissing(arr, n):
    N = 100000
    vis = [0] * (2 * N + 5)
    for i in range(n):
        vis[N + arr[i]] = 1
    for i in range(1, N + 2):
        if vis[N + i] == 0:
            return i

t=int(input())

for j in range(t):
    n=int(input())
    arr=[int(i) for i in input().split()]
    ans = firstMissing(arr,n)

    print(ans)
