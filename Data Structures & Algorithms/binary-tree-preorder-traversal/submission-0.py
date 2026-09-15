# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []

        def recur(curr):
            ans.append(curr.val)
            if curr.left:
                recur(curr.left)
            if curr.right:
                recur(curr.right)

        recur(root)
        return ans
