from os import *
from sys import *
from collections import *
from math import *

def findPosition(arr, n, k):

	for i in range(n):
		if arr[i] == k:
			return i
	return -1