from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def reverseStack(stack) :
	
	stack.reverse()
	return stack

# taking input
def takeInput() :

	n = int(input().strip())
	if(n == 0) :
		 return list(), n

	stack = list(map(int,stdin.readline().strip().split(" ")))
	return stack, n

def printStack(stack) :

	while(len(stack) > 0) :

		print(stack.pop(),end = " ")


# main
stack, n = takeInput()
reverseStack(stack)
printStack(stack)