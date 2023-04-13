from sys import stdin
import sys
import math

def evaluatePostfix(exp):
    n, MOD = len(exp), 1000000007
    G = []

    def modExp(a, p):
        ret = 1
        while p:
            if p & 1:
                ret = ret * a % MOD
            a = a * a % MOD
            p //= 2
        return ret

    for i in range(n):
        c = exp[i]
        if c == '+':
            b = G.pop()
            a = G.pop()
            G.append((a + b) % MOD)
        elif c == '-':
            b = G.pop()
            a = G.pop()
            G.append((a - b + MOD) % MOD)
        elif c == '*':
            b = G.pop()
            a = G.pop()
            G.append(a * b % MOD)
        elif c == '/':
            b = G.pop()
            a = G.pop()
            G.append(a * modExp(b, MOD - 2) % MOD)
        else:
            G.append(int(c))
    return G.pop()


# Taking the input.
def takeInput():
    exp = list(map(str, input().strip().split(" ")))
    return exp

# Main.
t = int(input())
while t:
    exp = takeInput()
    while("" in exp):
        exp.remove("")
    print(evaluatePostfix(exp))
    t = t-1
