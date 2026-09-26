# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def isSub(root, sub):
            if not root and not sub:
                return True

            if not root or not sub or root.val != sub.val:
                return False

            return isSub(root.left, sub.left) and isSub(root.right, sub.right)

        def dfs(root):
            if not root:
                return False
            
            if root.val == subRoot.val:
                if isSub(root, subRoot):
                    return True




            if dfs(root.left):
                return True
            if dfs(root.right):
                return True


            return False


        return dfs(root)