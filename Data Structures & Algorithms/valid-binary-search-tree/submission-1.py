# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        


        def recurse(root, lowerBound, higherBound):
            if not root:
                return True

            if not (root.val > lowerBound and root.val < higherBound):
                return False


            return recurse(root.left, lowerBound, root.val) and recurse(root.right, root.val, higherBound)

        


        return recurse(root, float("-inf"), float("inf"))


        