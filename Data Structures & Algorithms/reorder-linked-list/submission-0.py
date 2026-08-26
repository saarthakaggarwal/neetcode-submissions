# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        dummyNode = ListNode(val = 0, next = head)
        curNode = dummyNode
        slow = dummyNode

        while curNode and curNode.next: 
            slow = slow.next
            curNode = curNode.next.next 


        curNode = slow.next
        slow.next = None
        prev = None 
        while curNode:
            temp = curNode.next
            curNode.next = prev
            prev = curNode
            curNode = temp


        otherHead = prev
        dummyNode = ListNode(val = 0, next = head)
        curNode = dummyNode
        while head and otherHead:
            curNode.next = head
            head = head.next
            curNode = curNode.next
            curNode.next = otherHead
            otherHead = otherHead.next
            curNode = curNode.next

        if head:
            curNode.next = head

