import sys
from sys import stdin

def nthTermOfGP(n, a, r):
    MOD = 1000000007
    return pow(r, n - 1, MOD) * a % MOD

t = int(sys.stdin.readline().strip())

while(t > 0):
    n, a, r = map(int,input().split())
    print(nthTermOfGP(n,a,r))
    t = t - 1
    
    