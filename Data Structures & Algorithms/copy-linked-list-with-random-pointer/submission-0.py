"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        hm = {None : None}
        currNode = head
        while currNode:
            hm[currNode] = Node(x = currNode.val, next = None, random = None)
            currNode = currNode.next

        
        currNode = head
        while currNode:
            hm[currNode].next = hm[currNode.next]
            hm[currNode].random = hm[currNode.random]
            currNode = currNode.next

        return hm[head]