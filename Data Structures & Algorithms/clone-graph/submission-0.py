"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        

        visited = set()
        nodedict = {}

        def bfs(n):
            if not n:
                return
            queue = deque()
            queue.append(n)
            nodedict[n] = Node(n.val, [])
            visited.add(n)

            while queue:
                curNode = queue.popleft()
                

                for neigh in curNode.neighbors:
                    if neigh not in nodedict:
                        nodedict[neigh] = Node(neigh.val, [])
                    
                    nodedict[curNode].neighbors.append(nodedict[neigh])
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append(neigh)





        bfs(node)
        if not nodedict:
            return None
        return nodedict[node]