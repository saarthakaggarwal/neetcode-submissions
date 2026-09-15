# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_length = 0
        curr_length = 0
        if not root:
            return 0
        
        def recur(curr, c_l, m_l):
            c_l += 1
            max_length = max(m_l, c_l)
            
            if curr.left:
                max_length = max(max_length,recur(curr.left, c_l, m_l))
            if curr.right:
                max_length = max(max_length,recur(curr.right, c_l, m_l))
            
            
            c_l -= 1
            return max_length

        
        return recur(root, 0, 0)
            