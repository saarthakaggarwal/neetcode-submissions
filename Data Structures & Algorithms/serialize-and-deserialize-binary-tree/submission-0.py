# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(root):
            if not root:
                res.append("N")
                return

            
            res.append(f"{root.val}")
            dfs(root.left)

            

            dfs(root.right)

            return

        dfs(root)
        print(res)
        return " ".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        res = data.split()
        counter = 0

        def dfs():
            nonlocal counter
            
            if res[counter] == "N":
                return None

            root = TreeNode()
            root.val = res[counter]

            counter += 1
            root.left = dfs()

            counter += 1
            root.right = dfs()

            return root

        return dfs()

        
