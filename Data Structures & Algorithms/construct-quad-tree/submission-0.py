"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':


        def recurse(grid, currentNode):
            ROWS = len(grid)
            print(grid)
            cur = grid[0][0]
            leafNode = True
            for i in range(ROWS):
                for j in range(ROWS):
                    if grid[i][j] != cur:
                        leafNode = False
                        break 
            
            if leafNode:
                currentNode.isLeaf = True
                currentNode.val = 1 == cur
                return
            else:
                currentNode.topLeft = Node()
                currentNode.topRight = Node()
                currentNode.bottomLeft = Node()
                currentNode.bottomRight = Node()
                
                top_left = [row[:ROWS // 2] for row in grid[:ROWS // 2]]
                recurse([row[:ROWS // 2] for row in grid[:ROWS // 2]], currentNode.topLeft)
                recurse([row[ROWS // 2:] for row in grid[:ROWS // 2]], currentNode.topRight)
                recurse([row[:ROWS // 2] for row in grid[ROWS // 2:]], currentNode.bottomLeft)
                recurse([row[ROWS // 2:] for row in grid[ROWS // 2:]], currentNode.bottomRight)

            


        root = Node()
        recurse(grid, root)
        return root
