from os import *
from sys import *
from collections import *
from math import *
import re

def checkPalindrome(s):
	ans = re.sub('[^a-z0-9A-Z]+', '', s)
	ans = ans.upper()
	return ans == ans[::-1]
		
