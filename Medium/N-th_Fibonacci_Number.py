from os import *
from sys import *
from collections import *
from math import *

MOD = 1000000007

def multiply(a, b):
    ret = [[0, 0], [0, 0]]
    for i in range(0, 2):
        for j in range(0, 2):
            for k in range(0, 2):
                ret[i][j] += a[i][k] * b[k][j]
            ret[i][j] %= MOD
    return ret

def fibonacciNumber(n):
    if n <= 2:
        return 1
    a, ret = [[1, 1], [1, 0]], [[1, 0], [0, 1]]
    n -= 1
    while n:
        if n & 1:
            ret = multiply(ret, a)
        a = multiply(a, a)
        n //= 2
    return (ret[1][0] + ret[1][1]) % MOD
