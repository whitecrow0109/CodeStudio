def makeBeautiful(str):
	
	def getCnt(c):
		ans = 0
		cc = chr(ord('1') - ord(c) + ord('0'))
		for i in range(len(str)):
			if i & 1 and str[i] != c:
				ans += 1
			if (~i & 1) and str[i] != cc:
				ans += 1
		return ans
	
	return min(getCnt('0'), getCnt('1'))