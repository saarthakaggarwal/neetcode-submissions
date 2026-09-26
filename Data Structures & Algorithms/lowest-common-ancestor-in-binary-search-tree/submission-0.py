# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if p.val > q.val:
            a = q
            q = p
            p = a

        
        def dfs(root):
            if not root:
                return False

            if p.val <= root.val <= q.val:
                return root

            if q.val < root.val:
                return dfs(root.left)
            else:
                return dfs(root.right)
            
            



        return dfs(root)