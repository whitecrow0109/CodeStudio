from os import *
from sys import *
from collections import *
from math import *

n = int(input())
x = list(map(int, input().split()))
k = int(input())
ans = x[k:]
ans.extend(x[:k])
print(" ".join(str(val) for val in ans))