from os import *
from sys import *
from collections import *
from math import *
from queue import PriorityQueue

def reArrangeString(s):
    n = len(s)
    cnt = [0] * 33
    m = 0
    for i in range(n):
        idx = ord(s[i]) - ord('a')
        cnt[idx] += 1
        m = max(cnt[idx], m)
    if m > (n + 1) // 2:
        return "not possible"
    q = PriorityQueue()
    for i in range(0, 26):
        if cnt[i]:
            q.put((-cnt[i], chr(i + 97)))
    ans = ""
    while not q.empty():
        x = q.get()
        ans += x[1]
        if not q.empty():
            y = q.get()
            ans += y[1]
            if y[0] != -1:
                q.put((y[0] + 1, y[1]))
        if x[0] != -1:
            q.put((x[0] + 1, x[1]))
    return ans

