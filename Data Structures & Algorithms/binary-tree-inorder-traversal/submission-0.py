# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        def recur(curr):
            if(curr.left):
                recur(curr.left)
            
            ans.append(curr.val)

            if(curr.right):
                recur(curr.right)
                

        recur(root)
        return ans

            