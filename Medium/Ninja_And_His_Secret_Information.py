from os import *
from sys import *
from collections import *
from math import *

def encode(str):
    ans, n = "", len(str)
    for i in range(n):
        ans += chr(ord(str[i]) + 10)
    return ans

def decode(str):
    ans, n = "", len(str)
    for i in range(n):
        ans += chr(ord(str[i]) - 10)
    return ans
