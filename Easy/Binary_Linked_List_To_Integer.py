'''
    Following is the class structure of the Node class:
    
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
'''


def binaryToInteger(n: int, head) -> int:
    ans = 0
    while head is not None:
        ans = ans * 2 + head.data
        head = head.next
    return ans
