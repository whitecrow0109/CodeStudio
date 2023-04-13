from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :
    ansSum, nowSum = 0, 0
    for i in range(n):
        nowSum += arr[i]
        if ansSum < nowSum: ansSum = nowSum
        if nowSum < 0: nowSum = 0
    return ansSum

def takeInput() :	
    n =  int(input())
    if(n == 0) :
        return list(), n
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

arr, n = takeInput()
print(maxSubarraySum(arr, n))
