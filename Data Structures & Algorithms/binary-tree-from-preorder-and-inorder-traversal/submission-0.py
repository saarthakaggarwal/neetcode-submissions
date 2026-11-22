# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None


        
        hm = {}

        for i, val in enumerate(inorder):
            hm[val] = i


        preCounter = 0


        def build(l, r):
            nonlocal preCounter
            if l > r:
                return None

            rootVal = preorder[preCounter]
            root = TreeNode(val = rootVal)

            mid = hm[rootVal]
            preCounter += 1

            root.left = build(l, mid - 1)
            root.right = build(mid+1, r)

            return root


        return build(0, len(inorder) - 1)