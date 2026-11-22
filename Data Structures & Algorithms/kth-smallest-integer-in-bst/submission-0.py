# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        


        res = []


        def recurse(root):
            if not root:
                return


            recurse(root.left)

            res.append(root.val)

            recurse(root.right)

            return

        recurse(root)
        return res[k - 1]

