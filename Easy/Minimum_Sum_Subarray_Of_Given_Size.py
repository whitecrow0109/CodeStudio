from os import *
from sys import *
from collections import *
from math import *

def minSubarraySum(arr, n, k):

	num, cur = [0], 0
	for i in range(n):
		cur += arr[i]
		num.append(cur)
	ans = 1000000000000
	for i in range(0, n - k + 1):
		ans = min(ans, num[i + k] - num[i])
	return ans