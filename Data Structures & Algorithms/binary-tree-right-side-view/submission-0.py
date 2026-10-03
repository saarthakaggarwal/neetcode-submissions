# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

        inorder = []

        def recurse(root, level):
            if not root:
                return

            if level >= len(inorder):
                inorder.append([])
            
            inorder[level].append(root.val)

            recurse(root.left, level + 1)
            recurse(root.right, level + 1)

    
        recurse(root, 0)
        res = []

        for l in inorder:
            res.append(l[-1])
        return res