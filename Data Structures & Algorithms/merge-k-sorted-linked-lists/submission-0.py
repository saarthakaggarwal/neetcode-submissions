# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        return self.divide(lists, 0, len(lists) -1)

    def divide(self, lists, l, r):
        if l > r:
            return None
        if l == r:
            return lists[l]


        mid = (l + r) // 2
        left = self.divide(lists, l , mid)
        right = self.divide(lists, mid + 1, r)

        return self.conquer(left, right)

    def conquer(self, left, right):
        dummy = curr = ListNode()
        lhead, rhead = left, right

        while lhead and rhead:
            if lhead.val < rhead.val:
                curr.next = lhead
                curr = curr.next
                lhead = lhead.next
            else:
                curr.next = rhead
                curr = curr.next
                rhead = rhead.next

        if lhead:
            curr.next = lhead
        
        if rhead:
            curr.next = rhead


        return dummy.next