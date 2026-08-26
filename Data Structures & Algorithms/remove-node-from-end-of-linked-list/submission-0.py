# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        currNode = head
        dummyNode = ListNode(val = 0, next = head)
        prev = dummyNode
        
        for i in range(n-1):
            currNode = currNode.next
            
        print(currNode.val)
        nthNode = head

        while currNode.next:
            currNode = currNode.next
            nthNode = nthNode.next
            prev = prev.next
        

        prev.next = prev.next.next
        return dummyNode.next

        