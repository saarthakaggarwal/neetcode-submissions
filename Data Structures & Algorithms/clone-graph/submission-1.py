"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return 
        hm = {}


        def bfs(node):
            visited = set()
            q = deque()
            q.append(node)
            visited.add(node)


            while q:
                node = q.popleft()

                if node not in hm:
                    hm[node] = Node(val = node.val)


                for n in node.neighbors:
                    if n not in hm:
                        hm[n] = Node(val = n.val)
                    hm[node].neighbors.append(hm[n])
                    if n not in visited:
                        q.append(n)
                        visited.add(n)


        bfs(node)
        return hm[node]
