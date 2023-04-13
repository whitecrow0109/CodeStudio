from os import *
from sys import *
from collections import *
from math import *

N = 1000005
chk = [0] * N
prm, p = [], [0, 0]

def init():
    for i in range(2, 1000):
        if chk[i] == 0:
            for j in range(i * i, N, i):
                chk[j] = 1
    for i in range(2, N):
        p.append(p[i - 1])
        if chk[i] == 0:
            prm.append(i)
            p[i] += 1
    

init()

for _ in range(int(input())):
    A, B, K = map(int, input().split(" "))
    cnt = p[A - 1] + K - 1
    if cnt >= len(prm) or prm[cnt] > B:
        print(-1)
    else: print(prm[cnt])
